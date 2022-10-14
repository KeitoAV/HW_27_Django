import csv
import json


def csv_to_json(csvFilePath: str, jsonFilePath: str, model_name: str):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            fixture_dict = {}
            fields_dict = {}
            for key, value in list(row.items())[1:]:
                if key == "is_published":
                    fields_dict[key] = bool(row[key])
                else:
                    fields_dict[key] = row[key]
            fixture_dict["model"] = "ads." + model_name
            fixture_dict["pk"] = row[list(row.keys())[0]]
            fixture_dict["fields"] = fields_dict

            jsonArray.append(fixture_dict)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(jsonArray, indent=4, ensure_ascii=False))


csv_to_json("categories.csv", "categories.json", "Cat")
csv_to_json("ads.csv", "ads.json", "Ad")
