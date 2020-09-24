# coding:utf8

import requests
requests.packages.urllib3.disable_warnings()
content = requests.request(method="get",url="http://www.baidu.com",data='')
# print(content.content)

class optionRequest():

    def send_request(self,url,method,data,header=""):
        # header = {'Referer':'http://api.nnzhp.cn/'}
        return requests.request(method=method, url=url, data=data,headers=header,verify=False)

