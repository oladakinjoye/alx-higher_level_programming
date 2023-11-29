#!/usr/bin/python3
"""Define a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cb = 0
    while cb < len(text) and text[cb] == ' ':
        cb += 1

    while cb < len(text):
        print(text[cb], end="")
        if text[cb] == "\n" or text[cb] in ".?:":
            if text[cb] in ".?:":
                print("\n")
            cb += 1
            while cb < len(text) and text[cb] == ' ':
                cb += 1
            continue
        cb += 1
