import csv
from datetime import datetime


def export_to_csv(loc_x, loc_y, vel_x, vel_y):
    now = datetime.now().strftime("%d-%m-%Y-at-%H-%M")
    file_name = now + '.csv'
    with open(file_name, mode='w', newline='') as csv_file:
        fields = ['Location - X (cm)', 'Location - Y (cm)', 'Velocity - X (cm/s)', 'Velocity - Y (cm/s)']
        writer = csv.DictWriter(csv_file, fieldnames=fields)

        print(len(loc_x))

        writer.writeheader()
        for i in range(0, len(vel_x)):
            writer.writerow({'Location - X (cm)': loc_x[i], 'Location - Y (cm)': loc_y[i],
                             'Velocity - X (cm/s)': vel_x[i], 'Velocity - Y (cm/s)': vel_y[i]})
