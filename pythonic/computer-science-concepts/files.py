import locale
import csv, io
import chardet

# default encoding of system
print(locale.getpreferredencoding())

with open('kyoto_restaurants.csv', mode='rb') as file:
    # raw_bytes = file.read()
    raw_bytes = io.BufferedReader.read(file, 4)
    detected_encoding = chardet.detect(raw_bytes)
    print("encoding:", detected_encoding)

# reading with right encoding
with open('kyoto_restaurants.csv', encoding='utf16') as file:
    rows = list(csv.reader(file))
    num_rows = len(rows)
    print("Nums of row:", num_rows)
    columns, first_row = rows[0], rows[1]
    print(columns, first_row)

# writing to file
with open('my_file.txt', mode='w') as file:
    file.write('first line\n')
    file.write('second line\n')

with open('my_file.txt', mode='a') as file:
    file.write('third line\n')
    file.write('line 4\n')

# convert to utf-8
with open('kyoto_restaurants.csv', encoding='utf16') as file:
    rows = list(csv.reader(file))

with open('kyoto_restaurants_utf8.csv', mode='w', encoding='utf8') as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)
