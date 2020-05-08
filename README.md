# onechampionship
Assignment for OneChampionship

1. SQL: 

One Championship conducts events in a stadium, each event many people visit it and the stats are saved as these columns: id, event_name, people_count

Take leverage in adding sample data yourself.
Please write a query to display the records which have 3 or more consecutive events and the amount of people more than 100(inclusive).

Steps to Execute:
-----------------

Execute the sql file in below order to get the output.

prakashbalraj/onechampionship/Events_DDL.sql
prakashbalraj/onechampionship/Events_DML.sql
prakashbalraj/onechampionship/Events_Query.sql

2. Data Parsing: 

Write code to extract data from **data.csv**.

The data contains four columns. The first column is the person identifier. The second column is the datetime the person entered the floor. The third column is the floor the person accessed. The fourth column specifies the building the floor is in.

Each row is considered a floor access event. Your task it to output each floor access event in json format. Each event should comply with the schema located in **schema.json**.

Steps to Execute:
-----------------

Install the below packages if not available.
pip install csv
pip install json

python data_parsing.py

output file will be generated here /prakashbalraj/onechampionship/data.json
