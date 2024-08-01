import os
import re

footer_re = re.compile(r"^Official KDE-(US|E) Yu-Gi-Oh! TRADING CARD GAME Tournament Policy - V\.[0-9]\.[0-9]\n$")

for f in os.listdir():
    if f.endswith(".txt"):
        with open(f, encoding="utf-8") as old_file:
            old_file_content = old_file.readlines()
        new_file_content = []
        skip_next = False
        for line in old_file_content:
            if footer_re.fullmatch(line):
                skip_next = True
                continue
            if skip_next:
                skip_next = False
                continue
            new_file_content.append(line)
        with open(f, "w", encoding="utf-8") as new_file:
            new_file.writelines(new_file_content)