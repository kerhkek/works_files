files = ['file1.txt', 'file2.txt', 'file3.txt']
combined_file = 'combined.txt'

with open(combined_file, 'w', encoding='utf-8') as outfile:
    for i, filename in enumerate(files):
        with open(filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
            outfile.write(content)
            if i < len(files) - 1:
                outfile.write("\n\n--- Разделитель ---\n\n")