import re

class MDFormatter:

  @staticmethod
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

  @staticmethod
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
  
  @staticmethod
  def formatNewLines(text):
    """
    Replaces all instances of three or more consecutive newlines with two newlines.
    """
    return re.sub(r'\n{3,}', '\n\n', text)
  
  @staticmethod
  def replaceTabWithSpace(text):
    """
    Replaces all tabs with spaces.
    """
    return text.replace('\t', '  ')