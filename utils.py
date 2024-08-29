
import re
from bs4 import BeautifulSoup


def parse_uid(uid_string):
    """ Extracts the UID from the UID string """
    pattern_uid = re.compile(r'\d+ \(UID (?P<uid>\d+)\)')
    match = pattern_uid.match(uid_string)
    return match.group('uid')


def parse_flags(flags_string):
    """ Extracts flags from the flags string """
    pattern_flags = re.compile(r'\d+ \(FLAGS \((?P<flags>.*)\)\)')
    match = pattern_flags.match(flags_string)
    return match.group('flags')


def parse_labels(labels_string):
    """ Extracts labels from the labels string """
    pattern_labels = re.compile(r'\d+ \(X-GM-LABELS \((?P<labels>.*)\)\)')
    match = pattern_labels.match(labels_string)
    return match.group('labels')


def extract_text(html_content):
    """
    Mail body is a HTML String and this function extracts the plain text content from the HTML content.
    And also performs some text sanitization like removing special characters, numbers, etc.
    """
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Get the plain text content
    plain_text = soup.get_text()

    # Break into lines and remove leading and trailing whitespace on each line
    lines = (line.strip() for line in plain_text.splitlines())

    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # Drop blank lines
    plain_text = '\n'.join(chunk for chunk in chunks if chunk)

    # remove numbers and special characters
    plain_text = re.sub(r'[^a-zA-Z\s]', '', plain_text)

    return plain_text

