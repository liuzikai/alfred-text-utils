#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def remove_single_linefeeds(text):
    result = []
    i = 0
    length = len(text)

    while i < length:
        if text[i] == '\n':
            # Check if the next character is also a linefeed
            if i + 1 < length and text[i + 1] == '\n':
                # Add both linefeeds to the result and skip ahead
                result.append('\n')
                result.append('\n')
                i += 2
            else:
                # Replace a single linefeed with a space
                result.append(' ')
                i += 1
        else:
            # Add the character to the result as is
            result.append(text[i])
            i += 1

    # Join the list into a single string and return it
    return ''.join(result)

if __name__ == '__main__':
    for line in sys.argv[1:]:
        print(remove_single_linefeeds(line))
