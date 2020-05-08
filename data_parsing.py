import csv
import json

data ={}
with open('/prakashbalraj/onechampionship/data.csv') as csv_file:
    res = csv.DictReader(csv_file)
    for row in res:
        id = row["Person Id"]
        data[id] = row

with open('/prakashbalraj/onechampionship/data.json','w+') as json_file:
    json_file.write(json.dumps(data,indent=4))
