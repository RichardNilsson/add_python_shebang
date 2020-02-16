#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for adding shebang and encoding to python files
"""
from os import stat
from sys import argv

SHEBANG = "#!/usr/bin/env python3\n"
ENCODING = "# -*- coding: utf-8 -*-\n"
MODULE_DOCSTRING = '"""\n[Module docstring]\n"""'
IF_NAME_MAIN = "\n\n\nif __name__ == '__main__':\n    pass\n"

RESULT = argv[1:]

NEEDED = None
for file in RESULT:
    with open(file=file, mode="r") as f:
        FIRST_LINE = f.readline()
        SECOND_LINE = f.readline()
        if FIRST_LINE == SHEBANG and SECOND_LINE == ENCODING:
            print("Shebang and encoding present in {file}.".format(file=file))
        elif FIRST_LINE == SHEBANG and SECOND_LINE != ENCODING:
            print(
                "Shebang present in {file}, but not encoding.".format(
                    file=file
                )
            )
            NEEDED = "encoding"
        else:
            print(
                "Shebang and encoding not present in {file}.".format(file=file)
            )
            NEEDED = "shebang and encoding"
    if NEEDED:
        with open(file=file, mode="r+") as f:
            if NEEDED == "encoding":
                LINES = f.readlines()
                LINES = LINES[1:]
            elif NEEDED == "shebang and encoding":
                LINES = f.readlines()
            LINES.insert(0, "{ENCODING}".format(ENCODING=ENCODING))
            LINES.insert(0, "{SHEBANG}".format(SHEBANG=SHEBANG))
            f.seek(0)
            f.writelines(LINES)
            print("Shebang inserted into {file}".format(file=file))
            if stat(file).st_size == 0:
                print(
                    "{file} is empty, inserting docstring".format(file=file)
                    + " and __name__ == __main__"
                )
                f.writelines(MODULE_DOCSTRING)
                f.writelines(IF_NAME_MAIN)

if not RESULT:
    print("You did not choose a file.")
