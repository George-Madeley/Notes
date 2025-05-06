import re


class Markdown_Formatter:
  @staticmethod
  def format_tabs(text):
    """
    Some text contains single \xa0 whilst others contain \xa0 \xa0. This
    function identifies if the text uses single or double \xa0 and replaces it
    with \t.
    """
    # Use regex to identify if the text contains any single \xa0 (i.e., any \xa0
    # that is not followed by another \xa0)
    single = re.findall(r"(?!\xa0 )\xa0 (?!\xa0 )", text)

    # If single is empty, then the text contains double \xa0. Replace double
    # \xa0 with \t
    if not single:
      text = text.replace("\xa0 \xa0 ", "\t")
    else:
      text = text.replace("\xa0 ", "\t")

    # Replace all remaining \xa0 with \t
    text = text.replace("\xa0 ", "\t")
    text = text.replace("\xa0", "\t")

    return text

  @staticmethod
  def format_contents(text):
    """
    Formats the text to remove the page numbers and ids.
    """

    non_ending_contents_regex = re.compile(r"\[[^\[\]\(\)]+\n")
    matches = non_ending_contents_regex.findall(text)
    while len(matches) > 0:
      for match in matches:
        # replace the \n with a space
        match_no_return = match.replace("\n", " ")
        text = text.replace(match, match_no_return)
      matches = non_ending_contents_regex.findall(text)

    contents_regex = re.compile(r"\[.+? \[\d+\]\(#.+?\)\]\(#.+?\)")
    inner_regex = re.compile(r"\s\[\d+\]\(#.+?\)")
    # For each match of the contentsRegex, replace the innerRegex with an empty
    # string
    matches = contents_regex.findall(text)
    for match in matches:
      # find the text in match that matches the innerRegex and replace it with
      # an empty string
      inner_match = inner_regex.search(match)
      if inner_match:
        inner_match = inner_match.group()
        new_match = match.replace(inner_match, "")
        # Replace the old match with the new match
        text = text.replace(match, new_match)

    toc_regex = re.compile(r"#_Toc[0-9]+")
    matches = toc_regex.findall(text)
    for match in matches:
      text = text.replace(match, "#contents")

    return text

  @staticmethod
  def format_new_lines(text):
    """
    Replaces all instances of three or more consecutive newlines with two
    newlines.
    """
    return re.sub(r"\n{3,}", "\n\n", text)

  @staticmethod
  def replace_tabs_with_spaces(text):
    """
    Replaces all tabs with spaces.
    """
    return text.replace("\t", "  ")

  @staticmethod
  def format_lists(text):
    """
    Formats the lists in the text.
    """
    list_regex = r"\n-\s+"
    text = re.sub(list_regex, "\n- ", text)

    list_regex = r"\n\d\.\s+"
    # Replace all instances of listRegex with a newline followed by the same
    # number and a period and a space
    text = re.sub(list_regex, "\n1. ", text)

    return text

  @staticmethod
  def remove_unnumbered(text):
    """
    Removes the .unnumbered text from headings.
    """
    unnumbered_regex = re.compile(r"\s\{#[A-Za-z]+\s\.unnumbered\}")
    matches = unnumbered_regex.findall(text)
    for match in matches:
      text = text.replace(match, "")

    return text

  @staticmethod
  def format_images(text):
    pattern = (
      r"!\[(.*)\]\(.*media/image(\d+)\.png\)\{width=\".*\"\nheight=\".*\"\}"
    )
    replacement = r"![\1](media/image\2.png)"
    text = re.sub(pattern, replacement, text)
    return text

  @staticmethod
  def format_cover_page(text):
    pattern = r"\+.*\n.*>\s*(.*\w).*\|\n.*\n.*\n.*\n.*>\s*(.*\w).*\|\n.*\n.*>\s*(.*\w).*\|\n.*\n.*>\s*(.*\d).*\|\n.*\+"  # noqa: E501
    text = re.sub(pattern, r"# \1\n\n@ \2\n@ \3\n@ \4\n", text)
    text = text.replace("\n\n\n: Cover page info", "")
    return text

  @staticmethod
  def remove_format_table(text):
    pattern = r"\nThese notes use a range of different formatting for different purposes.\nThe following is each format and their purpose:\n\n\+(?:.*\n){15}.*\+\n"  # noqa: E501
    text = re.sub(pattern, "", text)
    return text

  @staticmethod
  def format_headings(text):
    """Adds an additional # to all headings but not to the first heading."""
    pattern = r"^(#+)"
    # Replace all instances of pattern with #\1
    text = re.sub(pattern, r"#\1", text, flags=re.MULTILINE)
    return text[1:]
