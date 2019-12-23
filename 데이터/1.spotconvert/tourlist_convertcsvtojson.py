import pandas as pd
import json

#지명,평점,상세설명,mapx,mapy,이미지링크,주소,카테고리
# class Spot(models.Model):
#     name = models.CharField(max_length=50)
#     rating = models.FloatField()
#     explain = models.TextField()
#     mapx = models.IntegerField()
#     mapy = models.IntegerField()
#     imagelink = models.TextField()
#     address = models.CharField(max_length=200)
#     category = models.TextField()
columns = [ 'name','rating','explain','mapx','mapy','imagelink','address','category' ]

fieldnames = ('지명','평점','상세설명','mapx','mapy','이미지링크','주소','카테고리')
csvfilename = '데이터\\geometry.csv'
rows = [] 

data = pd.read_csv(csvfilename, encoding='utf-8')
data.columns = columns
data.drop(['category'], axis='columns', inplace=True)
#print(data.head(5))
data_dict = data.to_dict(orient="records")
fixture_list = []

for i in range(1,len(list(data_dict))+1):
    fixture_dict = {
        'pk': i,
        'model': "bike.Spot",
        'fields': data_dict[i-1],
    }
    fixture_list.append(fixture_dict)

with open('데이터\\tour_final.json', 'w', encoding='utf-8') as f:
    json.dump(fixture_list, f, indent=4)
