import argparse
import os
import sys

import win32com.client as win32_client


def main():
  args = init_parser()
  # default to current folder
  if len(args.doc_path) < 1:
    args.doc_path = ["."]

  wd = open_word()
  run_macros(wd, args.doc_path, args)
  close_word(wd)


def init_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "macro_path",
    help="Path of the macro to run in Word",
  )
  parser.add_argument(
    "-r",
    "--recurse",
    action="store_true",
    help="""
    recursively search through subfolders when looking for docx files. (default:
    false)
    """,
  )
  parser.add_argument(
    "-s",
    "--suffix",
    help="customize the suffix for processed files. (default: _done)",
    default="_done",
    nargs="?",
  )
  parser.add_argument(
    "--save",
    help="wether to save the file after running the macro. (default: false)",
    action="store_true",
  )
  parser.add_argument(
    "--out",
    help="output folder for the processed files. (default: current folder)",
    default=".",
    nargs="?",
  )
  parser.add_argument(
    "doc_path",
    nargs=argparse.REMAINDER,
    help="""
    path/s to .docx files or a folders that contains .docx files. (default:
    current folder)
    """,
  )
  parser.epilog = """
  © 2021 - Paul McClintock - https://gist.github.com/plauk/1d26b3c6434a6b0fc44a9b213bf92d77
  """
  parser.usage = """
  run_macro.py [-h] [-r] [-s SUFFIX] macro_name *doc_path (*add as many as you
  want)
  """
  args = parser.parse_args()
  return args


def open_word():
  wd = win32_client.gencache.EnsureDispatch("Word.Application")
  wd.Visible = False
  return wd


def close_word(wd):
  wd.Quit()
  wd = None


def run_macros(wd, items, recurse, macro_path, save, out, suffix):
  for dp in items:
    dp = os.path.abspath(dp)  # convert to absolute path
    # if path is a folder, grab ALL docx files from folder
    # otherwise, just run this file

    if os.path.isdir(dp):
      # recursively (or not) call this function for all docx files in this
      # folder
      sub_items = (
        [
          os.path.join(dp, f)
          for f in os.listdir(dp)
          if f.endswith("docx") or os.path.isdir(os.path.join(dp, f))
        ]
        if recurse
        else [os.path.join(dp, f) for f in os.listdir(dp) if f.endswith("docx")]
      )
      run_macros(wd, sub_items, False, macro_path, save, out, suffix)  # recurse
    else:
      # open doc
      doc = wd.Documents.Open(dp)
      macro_name = load_macro(doc, macro_path, out)
      pth = doc.Path + wd.PathSeparator
      nm = doc.Name.split(".")[0]
      ext = "." + doc.Name.split(".")[1]
      print(f"Opened {nm}", f" from {pth}")

      # run macro
      print("Attempting to run macro: ", macro_name)
      wd.Application.Run(macro_name)

      # save as, close and clean up
      if save:
        print("saving and closing doc", nm)
        doc.SaveAs(pth + nm + suffix + ext)
      doc.Close()
      doc = None

  # clean up
  print("Closing Word")
  wd.Quit()
  wd = None


def load_macro(doc, macro_path, out):
  if not os.path.exists(macro_path):
    print(f"Cannot find {macro_path}")
    sys.exit(1)

  macro_name = os.path.basename(macro_path).split(".")[0]

  with open(macro_path, "r") as file:
    macro_code = file.read()

  # use regex to find ##media_dir## and replace with the args.out
  macro_code = macro_code.replace("##out_dir##", os.path.join(out, "code"))
  if not os.path.exists(os.path.join(out, "code")):
    os.makedirs(os.path.join(out, "code"))

  vba_project = doc.VBProject
  # Check if the macro already exists and remove it
  for component in vba_project.VBComponents:
    if component.Name == "Module1":  # Assuming the macro is stored in Module1
      code_module = component.CodeModule
      found = code_module.Find(macro_name)
      if found:
        start_line, num_lines = (
          code_module.ProcStartLine(macro_name, 0),
          code_module.ProcCountLines(macro_name, 0),
        )
        code_module.DeleteLines(start_line, num_lines)
      break
  else:
    # If the module does not exist, create it
    component = vba_project.VBComponents.Add(1)
    component.Name = "Module1"

  # Add VBA macro to the module
  component.CodeModule.AddFromString(macro_code)

  return macro_name


if __name__ == "__main__":
  main()
