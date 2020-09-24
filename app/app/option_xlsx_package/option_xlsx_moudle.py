# coding:utf8
import xlrd
import json

# 打开一个excel文件
obj_excel = xlrd.open_workbook(filename="../testcase/testcase.xlsx")
sheet_names = obj_excel.sheet_names()
print(sheet_names)
obj_sheet = obj_excel.sheet_by_name(sheet_names[0])
content = obj_sheet.row_values(rowx=1,start_colx=0,end_colx=2)
print(content)
print(obj_sheet.row_values(rowx=0))

class optionXlsx():


    def open_file(self,filename):
        """
        打开一个excel文件，返回打开的文件句柄
        """
        result = {
            "statu":0,
            "obj":None,
            "msg":"",
        }
        try:
            result["obj"] = xlrd.open_workbook(filename)
            result["msg"] = "文件打开成功"
        except FileNotFoundError:
            result["statu"] = 1
            result["msg"] = "文件未找到"

        return result

    def get_excel_sheet_names(self,obj):
        """
        返回sheet_name 的列表
        :param obj:
        :return:
        """
        result = {
            "statu":0,
            "sheet_names":[],
            "msg":"",
        }
        try:
            result["sheet_names"] = obj.sheet_names()
            result["msg"] = "获取sheet_name列表成功"
        except:
            result["statu"] = 1
            result["msg"] = "获取sheet_name列表失败"

        return result

    def get_excel_obj_sheet(self, obj,sheet_name):
        """
        返回一个sheet的对象
        :param obj:
        :return:
        """
        result = {
            "statu":0,
            "obj":None,
            "msg":"",
        }
        try:
            result["obj"] = obj.sheet_by_name(sheet_name)
            result["msg"] = "获取sheet对象成功"
        except:
            result["statu"] = 1
            result["msg"] = "获取sheet对象失败"

        return result

    def get_sheet_values(self,obj,rowx=0,start_colx=0,end_colx=1):
        """
        获取sheet单元格中的值
        :param obj: sheet对象
        :param rowx: 行
        :param start_colx:开始的列
        :param end_colx: 结束的列
        :return:
        """
        result = {
            "statu":0,
            "data":[],
            "msg":"",
        }
        try:
            result["data"] = obj.row_values(rowx,start_colx,end_colx)
            result["msg"] = "获取数据成功"
        except:
            result["statu"] = 1
            result["msg"] = "获取数据失败"

        return result

#
# obj_op_xlsx = optionXlsx()
# file_name = "../testcase/testcase.xlsx"
# # 打开文件
# obj_ex = obj_op_xlsx.open_file(filename=file_name)
# # 获取sheet的name
# sheet_name = obj_op_xlsx.get_excel_sheet_names(obj_ex["obj"])
# # 获取sheet的对象
# obj_sheet = obj_op_xlsx.get_excel_obj_sheet(obj_ex["obj"],sheet_name["sheet_names"][0])
# # 获取sheet表中的值
# content = obj_op_xlsx.get_sheet_values(obj_sheet["obj"],rowx=0)
# print(content)
#
#
# content = obj_op_xlsx.get_sheet_values(obj_sheet["obj"],rowx=1,start_colx=14,end_colx=15)
# print(content)
# print(type(content["data"]))
# result  = json.loads(content["data"][0])
# print(result)
#
# content = obj_op_xlsx.get_sheet_values(obj_sheet["obj"],rowx=4,start_colx=6,end_colx=7)
# print(content)
#
# content = obj_op_xlsx.get_sheet_values(obj_sheet["obj"],rowx=3,start_colx=10,end_colx=11)
# print(content)
# print(obj_sheet["obj"].merged_cells)
