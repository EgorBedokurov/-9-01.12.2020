import csv

file = open('tz_opendata_z01012020_po01122020.csv', encoding='utf-8')

with open('data_toyota.csv', 'w') as f:
    reader = csv.DictReader(file)
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Brand', 'Color', 'Year', 'Fuel'])
def car_model(writer, reader):
    for row in reader:
        if row == {'TOYOTA'}:
            writer.writerow(row['MODEL'], row['MAKE_YEAR'], row['FUEL'])
    return writer