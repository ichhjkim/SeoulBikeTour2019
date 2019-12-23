import pandas as pd
import json

# class Bicycle(models.Model):
#     idnum = models.IntegerField()
#     stationname = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     mapy = models.FloatField() #latitude
#     mapx = models.FloatField() #longitude
#     parkingnum = models.IntegerField()
#     possiblebikenum = models.IntegerField() -> 이건 생각좀 해보자.
columns = [ 'idnum','stationname','address','mapy','mapx','parkingnum', 'possiblebikenum' ]

fieldnames = ('대여소ID','대여소명','대여소주소','위도','경도','거치대수','사용가능한자전거')
csvfilename = '데이터\\seoulbikeinfo191209.csv'
rows = [] 

data = pd.read_csv(csvfilename, encoding='utf-8')
data.columns = columns
#print(data.head(5))
data_dict = data.to_dict(orient="records")
fixture_list = []

for i in range(1,len(list(data_dict))+1):
    fixture_dict = {
        'pk': i,
        'model': "bike.Bicycle",
        'fields': data_dict[i-1],
    }
    fixture_list.append(fixture_dict)

with open('데이터\\bike_location.json', 'w', encoding='utf-8') as f:
    json.dump(fixture_list, f, indent=4)
