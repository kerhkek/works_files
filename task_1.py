with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

num_lines = len(lines)

all_text = ''.join(lines)
words = all_text.split()
num_words = len(words)

with open('statistics.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(f'Количество строк: {num_lines}\n')
    outfile.write(f'Количество слов: {num_words}\n')