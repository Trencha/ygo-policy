import os

for f in os.listdir():
    if f.endswith(".txt"):
        with open(f, encoding="utf-8") as old_file:
            old_file_content = old_file.readlines()
        new_file_content = []
        prepend_next_line = ""
        for line in old_file_content:
            if line == "•\n" or line == "o\n" or line == "▪\n":
                prepend_next_line = line.replace("\n", " ")
            else:
                line = prepend_next_line + line
                prepend_next_line = ""
                new_file_content.append(line)
        with open(f, "w", encoding="utf-8") as new_file:
            new_file.writelines(new_file_content)