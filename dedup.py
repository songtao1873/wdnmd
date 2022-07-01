file_read = open("./data/changfeng.txt", 'r', encoding="utf-8")
file_raw = file_read.read()
file_lines = file_raw.split('\n')
file_content_new = []
for line in file_lines:
    if line not in file_content_new:
        file_content_new.append(line)
    else:
        continue
file_content_new_formatted = '\n'.join(file_content_new)
print(file_content_new_formatted)
file_write = open("./data/changfeng.txt", 'w', encoding="utf-8")
file_write.write(file_content_new_formatted)
