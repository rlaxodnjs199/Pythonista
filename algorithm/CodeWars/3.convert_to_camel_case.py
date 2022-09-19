# Problem:
# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples:
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re


def to_camel_case_1(text):
    word_list = re.split("-|_", text)
    word1 = word_list[0]
    return word1 + "".join(word.capitalize() for word in word_list[1:])


def to_camel_case_2(text):
    return re.sub("[-_](.)", lambda word: word.group(1).upper(), text)
