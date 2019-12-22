import csv
import json


def csvtojson(src, dst):
    with open(src) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(dst, "w") as f:
        json.dump(rows, f)


csvtojson("test.csv", "test.file.json")

