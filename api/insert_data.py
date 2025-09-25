import csv

def insert_data(file_path: str, image_class: str, group: str, weight: str):
    print(f"file path: {file_path} -- image_class:{image_class}")

    with open('training.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([file_path, image_class, group, weight])
        

