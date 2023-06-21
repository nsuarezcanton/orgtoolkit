from datetime import datetime
import click
import csv
import os
import sys

csv.field_size_limit(sys.maxsize)


def write_csv(items: list[dict], file_prefix: str):
    try:
        os.mkdir("output")
    except FileExistsError:
        click.echo("./output directory is already created.")
    now = datetime.today().strftime("%Y%m%d-%H%M%S")
    csv_filename = "output/" + file_prefix + "_" + now + ".csv"
    csv_file = open(csv_filename, "w")
    csv_writer = csv.DictWriter(csv_file, items[0].keys())
    csv_writer.writeheader()
    for user in items:
        csv_writer.writerow(user)
    csv_file.close()
    click.echo("User list saved to " + os.getcwd() + "/" + csv_filename)


def read_csv(filename: str):
    return [row for row in csv.DictReader(open(filename))]
