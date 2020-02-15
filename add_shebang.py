#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for adding shebang and encoding to python files
"""
from os import listdir

from bullet import Check

SHEBANG = "#!/usr/bin/env python3\n"
ENCODING = "# -*- coding: utf-8 -*-\n"

ALL_FILES = listdir(path=".")

PYTHON_FILES = [file for file in ALL_FILES if file.endswith(".py")]

CLI = Check(prompt="Choose an option:", choices=PYTHON_FILES)

RESULT = CLI.launch()

NEEDED = None
for file in RESULT:
    with open(file=file, mode="r") as f:
        FIRST_LINE = f.readline()
        SECOND_LINE = f.readline()
        if FIRST_LINE == SHEBANG and SECOND_LINE == ENCODING:
            print(f"Shebang and encoding present in {file}.")
        elif FIRST_LINE == SHEBANG and SECOND_LINE != ENCODING:
            print(f"Shebang present in {file}, but not encoding.")
            NEEDED = "encoding"
        else:
            print(f"Shebang and encoding not present in {file}.")
            NEEDED = "shebang and encoding"

if not RESULT:
    print("You did not choose a file.")

if NEEDED:
    for file in RESULT:
        with open(file=file, mode="r+") as f:
            if NEEDED == "encoding":
                LINES = f.readlines()
                LINES = LINES[1:]
            elif NEEDED == "shebang and encoding":
                LINES = f.readlines()
            LINES.insert(0, f"{ENCODING}")
            LINES.insert(0, f"{SHEBANG}")
            f.seek(0)
            f.writelines(LINES)
            print("Shebang inserted into {file}")
