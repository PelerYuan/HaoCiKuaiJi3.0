import csv


def open_csv(file_path:str):
    """
    :param file_path:
    :return: [{'Name': 'Alice', 'Age': '30', 'City': 'New York'},
              {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'},
              {'Name': 'Charlie', 'Age': '35', 'City': 'Chicago'}]
    """
    data_list = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list

def write_csv(file_path:str, data_list:list):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        if data_list:
            fieldnames = data_list[0].keys()
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data_list)