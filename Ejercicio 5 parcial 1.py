import json
x = '{"main":{"temp":296.88,"feels_like":297.35,"temp_min":296.88,"temp_max":296.88,"pressure":1014,"humidity":78},"visibility":10000,"wind":{"speed":1.03,"deg":0},"clouds":{"all":40},"dt":1646948100,"sys":{"type":1,"id":8581,"country":"CO","sunrise":1646910092,"sunset":1646953451},"timezone":-5000,"id":3688465,"name":"Bucaramanga","cod":200}}'
y = json.dumps(x)
print(y)
