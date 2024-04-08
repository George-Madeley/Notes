import os
import re
import subprocess

from odf import text, teletype
from odf.opendocument import load

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
  mdDirectory = os.path.join(os.getcwd(), 'Markdown')
  mediaDirectory = os.path.join(mdDirectory, 'Media')

  os.makedirs(docxDirectory, exist_ok=True)
  os.makedirs(mdDirectory, exist_ok=True)
  os.makedirs(mediaDirectory, exist_ok=True)

  docxFiles = ['GM01613 - React.docx']

  for docxFile in docxFiles:
    filename = docxFile.split('.')[:-1]
    filename = ''.join(filename)

    mediaDirectory = os.path.join(mdDirectory, 'Media', filename)
    os.makedirs(mediaDirectory, exist_ok=True)

    docxToMd(filename, mdDirectory, docxDirectory, mediaDirectory)
    os.chdir(codeDirectory)
    # extractEmbeddedFiles(filename, docxDirectory, mdDirectory, mediaDirectory)
    os.chdir(notesDirectory)
    replaceText(mdDirectory, filename, mediaDirectory)

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
    odtText = formatTabs(odtText)

    if "export const useToggle" in odtText:
      print("Found")

    # Get ht odtFile name without the extension
    odtFileName = odtFile.split('.')[0]
    searchText = f'![]({mediaDirectory}/media/image{odtFileName}.emf)'
    
    replacementText = '```\n' + odtText + '```\n'
    if searchText in mdText:
      print(f"Found Text")
    mdText = mdText.replace(searchText, replacementText)

  mdText = formatContents(mdText)

  with open(os.path.join(mdDirectory, filename + '-new' + '.md'), 'w') as file:
    file.write(mdText)

def formatTabs(Text):
  """
  Some text contains single \xa0 whilst others contain \xa0 \xa0. This function
  identifies if the text uses single or double \xa0 and replaces it with \t.
  """
  # Use regex to identify if the text contains any single \xa0 (i.e., any \xa0
  # that is not followed by another \xa0)
  single = re.findall(r'(?!\xa0 )\xa0 (?!\xa0 )', Text)

  # If single is epmty, then the text contains double \xa0. Replace double \xa0
  # with \t
  if not single:
    Text = Text.replace('\xa0 \xa0 ', '\t')
  else:
    Text = Text.replace('\xa0 ', '\t')

  # Replace all remaining \xa0 with \t
  Text = Text.replace('\xa0 ', '\t')
  Text = Text.replace('\xa0', '\t')

  return Text

def formatContents(text):
  """
  Formats the text to remove the page numbers and ids.
  """

  nonEndingContentsRegex = re.compile(r'\[[^\[\]\(\)]+\n')
  matches = nonEndingContentsRegex.findall(text)
  while len(matches) > 0:
    for match in matches:
      # replace the \n with a space
      matchNoReturn = match.replace('\n', ' ')
      text = text.replace(match, matchNoReturn)
    matches = nonEndingContentsRegex.findall(text)

  contentsRegex = re.compile(r'\[.+? \[\d+\]\(#.+?\)\]\(#.+?\)')
  innerRegex = re.compile(r'\s\[\d+\]\(#.+?\)')
  # For each match of the contentsRegex, replace the innerRegex with an empty
  # string
  matches = contentsRegex.findall(text)
  for match in matches:
    # find the text in match that matches the innerRegex and replace it with 
    # an empty string
    innerMatch = innerRegex.search(match)
    if innerMatch:
      innerMatch = innerMatch.group()
      newMatch = match.replace(innerMatch, '')
      # Replace the old match with the new match
      text = text.replace(match, newMatch)

  return text


if __name__ == '__main__':
  main()
