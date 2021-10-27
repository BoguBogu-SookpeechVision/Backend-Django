import json
import csv
import os

# add headers to a new csv file
f = open('file.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerow(['mouth_width', 'mouth_height', 'upper_lip', 'lower_lip', 'cheek_chin', 'cheek_cheek', 'shape'])

# make image file names into a list
all_files = os.listdir('./new_lip_shape_json/eu/new')

# loop through all files and calculate distances
for file in all_files:
    with open(f'./new_lip_shape_json/eu/new/{file}', 'r') as f:
        json_data = json.load(f)

    # width and height of lips
    m_width = json_data['54'][0] - json_data['48'][0]
    m_height = json_data['57'][1] - json_data['51'][1]

    # thickness of upper and lower lip
    upper_lip = json_data['62'][1] - json_data['51'][1]
    lower_lip = json_data['57'][1] - json_data['66'][1]

    # distance between the cheek and chin
    cheek_chin = json_data['8'][1] - json_data['2'][1]

    # distance between right and left cheek
    cheek_cheek = json_data['14'][0] - json_data['2'][0]

    f = open('file.csv', 'a', newline='')
    wr = csv.writer(f)

    wr.writerow([m_width, m_height, upper_lip, lower_lip, cheek_chin, cheek_cheek, 'lip_shape'])


