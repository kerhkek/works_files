search_word = input("Введите слово для поиска: ")

found = False
count = 0
lines_with_word = []

with open('text.txt', 'r', encoding='utf-8') as infile:
    for line_number, line in enumerate(infile, start=1):
        if search_word in line:
            found = True
            count += line.count(search_word)
            lines_with_word.append(line_number)

if found:
    print(f"Слово '{search_word}' найдено.")
    print(f"Количество встреч: {count}")
    print(f"Встречается в строках: {lines_with_word}")
else:
    print(f"Слово '{search_word}' не найдено.")

with open('search_results.txt', 'w', encoding='utf-8') as outfile:
    if found:
        outfile.write(f"Слово '{search_word}' найдено.\n")
        outfile.write(f"Количество встреч: {count}\n")
        outfile.write(f"Встречается в строках: {lines_with_word}\n")
    else:
        outfile.write(f"Слово '{search_word}' не найдено.\n")