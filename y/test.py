import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
    'Content-Type': 'application/json,charset=utf-8',
    'Accept': 'application/json',
    'xweb_xhr': '1',
    'channel': 'GuanWang',
    'os': 'miniprogram',
    'token': '0698f70c-a244-43cd-883c-07fda0717546',
    'appVersion': '7.0.0',
    'appVersion': '7.0.0',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wx5e3ebf9e57378d9d/53/page-frame.html',
    'Accept-Language': 'en-us,en',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Length': '905'

}

data = {
    "is_return": 0, "appointment_timestamp": 0, "is_change_driver": 0, "mileage_total": 53.7, "locations": [{"index": 0, "province_id": 440000, "city_id": 440600, "county_id": 440605, "town_id": 440605100, "longitude": 113.162838, "latitude": 23.132093, "is_start_location": 1, "is_end_location": 0, "mobile": "13555555555", "user_name": "", "address": "佛山市力进物流园", "full_region_name": "广东省佛山市南海区里水镇", "building_address": "", "city": "佛山市", "county": "南海区"}, {"index": 1, "province_id": 440000, "city_id": 440100, "county_id": 440118, "town_id": 440118004, "longitude": 113.591156, "latitude": 23.178835, "is_start_location": 0, "is_end_location": 1, "mobile": "", "user_name": "", "address": "增城永宁街道人大代表永和社区联络站", "full_region_name": "广东省广州市增城区永宁街道", "building_address": "", "city": "广州市", "county": "增城区"}], "weight": 0, "volume": 0, "region_vehicle_id": 20634
}

response = requests.post(
    url='https://configs-api.huitouche.com/pricing', headers=headers, data=json.dumps(data))

print(response)
print(response.text)
with open(r'D:\project\test\y\r3.txt', 'w') as f:
    f.write(response.text)
