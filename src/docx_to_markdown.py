import os
import subprocess
import argparse
import sys
import tempfile

from odf import text as odf_text, teletype
from odf.opendocument import load as odf_load

from utils import chdir
from run_macro import run_macros, open_word, close_word

from formatter import Markdown_Formatter


def main():
  cwd = os.getcwd()
  path = chdir()
  if os.name == "nt":
    input_paths = os.path.join(
      "C:\\",
      "Users",
      "George",
      "OneDrive",
      "Documents",
      "Personal",
      "Notes",
      "Typed",
    )
    output_directory = os.path.abspath(os.path.join(path, "..", "output"))
    pandoc = os.path.abspath(
      os.path.join(
        tempfile.gettempdir(),
        "..",
        "..",
        "Roaming",
        "local",
        "bin",
        "pandoc.exe",
      )
    )

  parser = argparse.ArgumentParser(
    description="""
    This tool aims to convert word documents in to markdown documents. Most
    tools that perform this job neglect embedded documents. This aims to extract
    the contents of the embedded documents and add them as text and/or images to
    the final markdown document.
    """
  )
  parser.add_argument(
    "-i",
    "--input_paths",
    help=f"The list of files to convert (default: {input_paths})",
    nargs="*",
    type=str,
    default=input_paths,
  )
  parser.add_argument(
    "-o",
    "--out_directory",
    help=f"The output file location (default: {output_directory})",
    nargs="?",
    type=str,
    default=output_directory,
  )
  parser.add_argument(
    "--pandoc",
    help=f"Path to the pandoc executable (default: {pandoc})",
    nargs="?",
    type=str,
    default=pandoc,
  )
  args = parser.parse_args()

  if args.input_paths != input_paths:
    if isinstance(args.input_paths, list):
      for index in range(len(args.input_paths)):
        args.input_paths[index] = os.path.abspath(
          os.path.join(cwd, args.input_paths[index])
        )
    else:
      args.input_paths = os.path.abspath(os.path.join(cwd, args.input_paths))

  if args.out_directory != output_directory:
    args.out_directory = os.path.abspath(os.path.join(cwd, args.out_directory))

  if not os.path.exists(args.out_directory):
    os.makedirs(args.out_directory, exist_ok=True)

  convertFiles(args)


def convertFiles(args):
  docx_files = get_docx_files(args)

  for docx_file in docx_files:
    filename = os.path.basename(docx_file).split(".")[0]

    file_dir = os.path.join(args.out_directory, filename)
    os.makedirs(file_dir, exist_ok=True)

    out_file_path = os.path.join(file_dir, filename + ".md")

    docx_to_md(args, docx_file, out_file_path, file_dir)
    extract_embedded_files(docx_file, file_dir)
    add_embedded_file_content(out_file_path, file_dir)
    remove_done_file(filename, os.path.dirname(docx_file))


def get_docx_files(args):
  files = []
  if isinstance(args.input_paths, list):
    for path in args.input_paths:
      if os.path.isdir(path):
        files.extend(
          [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.endswith(".docx")
          ]
        )
      elif os.path.isfile(path):
        files.append(path)
  else:
    if os.path.isdir(args.input_paths):
      files.extend(
        [
          os.path.join(args.input_paths, f)
          for f in os.listdir(args.input_paths)
          if f.endswith(".docx")
        ]
      )
    elif os.path.isfile(args.input_paths):
      files.append(args.input_paths)
  return files


def docx_to_md(args, input_file_path, out_file_path, file_dir):
  print(f"Converting {os.path.basename(input_file_path)} to markdown...")

  if not os.path.exists(args.pandoc):
    print(f"Cannot find {args.pandoc}")
    sys.exit(1)

  try:
    subprocess.run(
      [
        "pandoc",
        "--extract-media",
        file_dir,
        input_file_path,
        "-o",
        out_file_path,
      ],
      check=True,
    )
  except subprocess.CalledProcessError:
    print(f"Error converting {os.path.basename(input_file_path)} to markdown")
    return
  print("Done!")


def extract_embedded_files(file_path, file_dir):
  path = chdir()
  print(f"Extracting embedded files from {os.path.basename(file_path)}...")
  if not os.path.exists(file_path):
    print(f"Cannot find {file_path}.docx")
    return

  macro_path = os.path.abspath(
    os.path.join(path, "..", "scripts", "ExtractAndSaveEmbeddedFiles.vb")
  )
  if not os.path.exists(macro_path):
    print(f"Cannot find {macro_path}")
    sys.exit(1)

  macro_runner = os.path.abspath(os.path.join(path, "run_macro.py"))
  if not os.path.exists(macro_runner):
    print(f"Cannot find {macro_runner}")
    sys.exit(1)

  wd = open_word()
  run_macros(wd, [file_path], False, macro_path, False, file_dir, "_done")
  close_word(wd)
  print("Done!")


def add_embedded_file_content(out_file_path, file_dir):
  if not os.path.exists(out_file_path):
    print(f"Cannot find {out_file_path}")
    return

  with open(out_file_path, "r") as file:
    md_content = file.read()

  odt_files = [f for f in os.listdir(file_dir) if f.endswith(".odt")]

  for odt_file in odt_files:
    # get the text from the odt file
    odt_content = odf_load(os.path.join(file_dir, odt_file))
    odt_text = ""
    for para in odt_content.getElementsByType(odf_text.P):
      odt_text += teletype.extractText(para) + "\n"

    # Replace \xa0 with \t
    odt_text = Markdown_Formatter.format_tabs(odt_text)
    language = "text"

    # Get ht odtFile name without the extension
    odt_file_name = os.path.basename(odt_file).split(".")[0]
    searchText = f"![]({file_dir}/media/image{odt_file_name}.emf)"

    replacement_text = "```" + language + "\n" + odt_text + "```\n"
    md_content = md_content.replace(searchText, replacement_text)

  md_content = Markdown_Formatter.format_contents(md_content)
  md_content = Markdown_Formatter.format_new_lines(md_content)
  md_content = Markdown_Formatter.replace_tabs_with_spaces(md_content)
  md_content = Markdown_Formatter.format_lists(md_content)
  md_content = Markdown_Formatter.remove_unnumbered(md_content)

  with open(out_file_path, "w") as file:
    file.write(md_content)


def remove_done_file(filename, input_dir):
  print(f"Removing {os.path.basename(filename)}_done.docx...")
  if os.path.exists(os.path.join(input_dir, filename + "_done.docx")):
    os.remove(os.path.join(input_dir, filename + "_done.docx"))


# ---------------------------------------------------------------------------- #
#                                  entry point                                 #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
  main()
