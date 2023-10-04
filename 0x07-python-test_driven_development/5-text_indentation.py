#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    content = 0
    while content < len(text) and text[content] == ' ':
        content += 1

    while content < len(text):
        print(text[content], end="")
        if text[content] == "\n" or text[content] in ".?:":
            if text[content] in ".?:":
                print("\n")
            content += 1
            while content < len(text) and text[content] == ' ':
                content += 1
            continue
        content += 1
