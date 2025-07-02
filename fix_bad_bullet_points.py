import os

for f in os.listdir():
    if f.endswith(".txt"):
        with open(f, encoding="utf-8") as old_file:
            old_file_content = old_file.readlines()
        new_file_content = []
        add_bullet_next_line = False
        for line in old_file_content:
            if line == "•\n":
                add_bullet_next_line = True
            else:
                if add_bullet_next_line:
                    line = "• " + line
                    add_bullet_next_line = False
                new_file_content.append(line)
        with open(f, "w", encoding="utf-8") as new_file:
            new_file.writelines(new_file_content)