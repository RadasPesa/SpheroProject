import csv
from datetime import datetime


def export_to_csv():
    now = datetime.now().strftime("%d-%m-%Y-at-%H-%M")
    file_name = now + '.csv'
    with open(file_name, mode='w', newline='') as csv_file:
        fields = ['time', 'location']
        writer = csv.DictWriter(csv_file, fieldnames=fields)

        writer.writeheader()
        writer.writerow({'time': '0.0', 'location': '0.0'})
