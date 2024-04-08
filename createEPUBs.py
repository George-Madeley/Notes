import os
import subprocess

from odf import text, teletype
from odf.opendocument import load

from markdownFormatting import MDFormatter

def main():
  # Change the current working directory to the C drive
  codeDirectory = os.getcwd()
  notesDirectory = os.path.join(
      'C:\\',
      'Users',
      'Georg',
      'OneDrive',
      'Documents',
      'Personal',
      'Notes')
  os.chdir(notesDirectory)

  docxDirectory = os.path.join(os.getcwd(), 'Typed')
  epubDirectory = os.path.join(os.getcwd(), 'EPUBs')
  mdDirectory = os.path.join(os.getcwd(), 'Markdown')
  mediaDirectory = os.path.join(mdDirectory, 'Media')

  os.makedirs(docxDirectory, exist_ok=True)
  os.makedirs(epubDirectory, exist_ok=True)
  os.makedirs(mdDirectory, exist_ok=True)
  os.makedirs(mediaDirectory, exist_ok=True)

  docxFiles = ['GM01613 - React.docx', 'GM01614 - Redux.docx']

  for docxFile in docxFiles:
    filename = docxFile.split('.')[:-1]
    filename = ''.join(filename)

    mediaDirectory = os.path.join(mdDirectory, 'Media', filename)
    os.makedirs(mediaDirectory, exist_ok=True)

    docxToMd(filename, mdDirectory, docxDirectory, mediaDirectory)
    os.chdir(codeDirectory)
    extractEmbeddedFiles(filename, docxDirectory, mdDirectory, mediaDirectory)
    os.chdir(notesDirectory)
    replaceText(mdDirectory, filename, mediaDirectory)
    mdToEpub(mdDirectory, epubDirectory, filename)

def docxToMd(filename, mdDirectory, docxDirectory, mediaDirectory):
  print(f"Converting {filename}.docx to markdown...")

  docxFilepath = os.path.join(docxDirectory, filename + '.docx')
  mdFilePath = os.path.join(mdDirectory, filename + '.md')

  # Convert the docx file to markdown
  args = [
      'pandoc',
      '--extract-media',
      mediaDirectory,
      docxFilepath,
      '-o',
      mdFilePath]
  subprocess.Popen(args)

  print(f"Converted {filename}.docx to markdown")


def extractEmbeddedFiles(filename, docxDirectory, mdDirectory, mediaDirectory):
  print(f"Extracting embedded files from {filename}.docx...")

  docxFilepath = os.path.join(docxDirectory, filename + '.docx')

  if not os.path.exists(docxFilepath):
    print(f"Cannot find {filename}.docx")
    return


  # Extract the embedded files from the docx file
  command = f'python run_macro.py "ExtractAndSaveEmbeddedFiles" "{docxFilepath}"'
  os.system(command)

  print(f"Extracted embedded files from {filename}.docx")
  
def replaceText(mdDirectory, filename, mediaDirectory):
  with open(os.path.join(mdDirectory, filename + '.md'), 'r') as file:
    mdText = file.read()

  odtFiles = [f for f in os.listdir(mediaDirectory) if f.endswith('.odt')]

  for odtFile in odtFiles:
    # get the text from the odt file
    textdoc = load(os.path.join(mediaDirectory, odtFile))
    odtText = ''
    for para in textdoc.getElementsByType(text.P):
      odtText += teletype.extractText(para) + '\n'

    # Replace \xa0 with \t
    odtText = MDFormatter.formatTabs(odtText)
    language = 'text'
    
    # Get ht odtFile name without the extension
    odtFileName = odtFile.split('.')[0]
    searchText = f'![]({mediaDirectory}/media/image{odtFileName}.emf)'
    
    replacementText = '```' + language + '\n' + odtText + '```\n'
    mdText = mdText.replace(searchText, replacementText)

  mdText = MDFormatter.formatContents(mdText)
  mdText = MDFormatter.formatNewLines(mdText)
  mdText = MDFormatter.replaceTabWithSpace(mdText)
  mdText = MDFormatter.formatLists(mdText)
  mdText = MDFormatter.removeUnnumbered(mdText)

  with open(os.path.join(mdDirectory, filename + '.md'), 'w') as file:
    file.write(mdText)

def mdToEpub(mdDirectory, epubDirectory, filename):
  print(f"Converting {filename}.md to {filename}.epub...")

  mdFilePath = os.path.join(mdDirectory, filename + '.md')
  epubFilePath = os.path.join(epubDirectory, filename + '.epub')

  # Convert the markdown file to epub
  args = [
      'pandoc',
      mdFilePath,
      '-o',
      epubFilePath]
  subprocess.Popen(args)

  print(f"Converted {filename}.md to {filename}.epub")

if __name__ == '__main__':
  main()
