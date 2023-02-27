import csv
import json


def csv_reader(file_location):
    with open(file_location, mode='r') as csv_file:
        data = [line for line in csv.DictReader(csv_file)]
        data = cast_map_data(data)

    return data


def json_reader(file_location):
    with open(file_location, mode='r') as json_file:
        data = [line for line in json.load(json_file)]
        data = cast_map_data(data)

    return data


def cast_map_data(data):
    for row in data:
        try:
            row['Lat'] = float(row['Lat'])
            row['Long'] = float(row['Long'])
            row['Altitude'] = float(row['Altitude'])
        except Exception as exp:
            raise ValueError(str(exp))

    return data
