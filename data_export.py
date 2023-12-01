import csv


def export_to_csv(data, filename, input_size):
    try:
        with open(filename, 'x', newline='') as csvfile:
            fieldnames = ["Input Size", "Average Time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    except FileExistsError:
        pass  # File already exists, do nothing

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ["Input Size", "Average Time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for row in data:
            writer.writerow({"Input Size": input_size, "Average Time": row})
