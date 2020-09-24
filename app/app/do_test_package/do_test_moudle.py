# coding:utf8
from app.option_xlsx_package.option_xlsx_moudle import  optionXlsx
from app.send_request_package.send_request_moudle import optionRequest
import json
# 执行用例的文件

obj_op_requ = optionRequest()

# 打开文件
file_name = "../testcase/testcase.xlsx"
# 创建一个操作excel的对象
obj_excel_op = optionXlsx()
# 打开excel文件
obj_excel = obj_excel_op.open_file(file_name)
# 获取sheet的对象
obj_sheet = obj_excel_op.get_excel_obj_sheet(obj_excel["obj"],"登录")["obj"]
# 第一行的标题
table_title = obj_excel_op.get_sheet_values(obj_sheet,rowx=0,start_colx=0,end_colx=30)
# print(table_title["data"].__len__())
# print(table_title["data"].index("用例编号"))
# url
url_index = table_title["data"].index("url")
url = obj_excel_op.get_sheet_values(obj_sheet,rowx=1,start_colx=url_index,end_colx=url_index+1)["data"][0]

method_index = table_title["data"].index("请求方法")
method = obj_excel_op.get_sheet_values(obj_sheet,rowx=1,start_colx=method_index,end_colx=method_index+1)["data"][0]

qingqiucanshu_index = table_title["data"].index("请求参数")
qingqiucanshu  = obj_excel_op.get_sheet_values(obj_sheet,rowx=1,start_colx=qingqiucanshu_index,end_colx=qingqiucanshu_index+1)["data"][0]


bodycanshu_index = table_title["data"].index("body参数")
bodycanshu  = obj_excel_op.get_sheet_values(obj_sheet,rowx=1,start_colx=bodycanshu_index,end_colx=bodycanshu_index+1)["data"][0]
bodycanshu = json.loads(bodycanshu)
# bodycanshu={
#     "v":"3.6.1",
#     "osv":"6.0.1",
#     "deviceToken":"B8:37:65:26:BA:1B",
#     "driverType":"OPPOR9s",
#     "client":"student",
#     "os":"Android",
#     "driverCode":"3.8.9",
#     "password":"f379eaf3c831b04de153469d1bec345e",
#     "username":"10278456",
#     "is_http":"1",
# }
response = obj_op_requ.send_request(url,method,data=bodycanshu)
print(response.content)
print(json.loads(response.content))

