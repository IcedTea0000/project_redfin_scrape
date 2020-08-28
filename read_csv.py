import csv
import logging


def extract_csv_to_list(file_path, csv_delimiter):
    try:
        file = open(file_path, 'r')
        reader = csv.reader(file, delimiter=csv_delimiter, skipinitialspace=True)
        reader = list(reader)

        # clean duplicate rows
        unique_data = []
        for row in reader:
            unique_data.append(tuple(row))
        unique_data = set(unique_data)

        file.close()
        return list(unique_data)

    except FileNotFoundError:
        logging.error('Directory or file not found')


if __name__ == '__main__':
    # execute only if run as a script
    file_path = 'C:/workspace/ProjectRedfinScrape/files/city_list.csv'
    test_data = extract_csv_to_list(file_path=file_path, csv_delimiter=',')
    print(test_data)
