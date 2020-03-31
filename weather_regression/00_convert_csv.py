input_csv = 'data.csv'
output_csv = 'kion.csv'

with open(input_csv, 'rt', encoding='utf-8') as csv_file:
    lines = csv_file.readlines()

# replace header
lines = ['year,month,day,tempreature,quality,homogeneus'] + ["\n"] + lines[1:]
lines = map(lambda value: value.replace('/', ','), lines)

result = ''.join(lines).strip()
print(result)

with open(output_csv, 'wt', encoding='utf-8') as csv_file:
    csv_file.write(result)
