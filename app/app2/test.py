# coding:utf8

# import ruamel.yaml
#
# with open("test.yaml","r",encoding="utf-8") as f:
#     try:
#         alldata = ruamel.yaml.safe_load(f)
#     except ruamel.yaml.YAMLError as exc:
#         print(exc)
#
# print(alldata)
#
# for data in  alldata:
#     print(data)
#     print(alldata[data][0]["id"])
#     print(alldata[data][0]["test_case_info"]["name"])

url = "https://172.17.20.30/student/User/login"
method="post"
headers = {
    "Host":"mapi.ekwing.com"
}
data = {
    "v":"3.6",
    "osv":"6.0.1",
    "deviceToken":"B8:37:65:26:BA:1B",
    "driverType": "OPPOR9s",
    "client": "student",
    "os": "Android",
    "driverCode": "3.8.9",
    "is_http": "1",
    "password":"f379eaf3c831b04de153469d1bec345e",
    "username":"10278316"

}
import requests

proxies={
    'http':'http://172.17.20.30:80',
    'https':'https://172.17.20.30:443',
}

response = requests.request(method=method,data=data,url= url,headers=headers,verify=False)
print(response.json())
# dict1 = {"小明":89,"小花":78}
# dict2 = {"小明":45}
# print({**dict1,**dict2})
# print({**dict2,**dict1})