# coding:utf8
from app2.stu_api_code.common.operationyaml import OperationYaml
from app2.stu_api_code.api_code.send_request_package.send_request_moudle import optionRequest
from app2.stu_api_code.common.assist import Assist
import json
from app2.stu_api_code.common.urlhandle import UrlHandle



class Login:

    """
    执行登录的测试用例的方法
    """

    def __init__(self,environment,host_dict={}):
        # 读取测试用例
        self.obj_yaml = OperationYaml("../login/login_test_case_"+environment+".yaml")
        # 获取测试用例的数据
        self.login_data = self.obj_yaml.get_yaml_data()
        # 获取发送请求的对象
        self.obj_request = optionRequest()
        # 获取辅助的函数操作
        self.obj_assist  = Assist(environment=environment,host_dict=host_dict)
        # 获取host配置字典
        self.host_dict = host_dict
        # 获取操作url的对象
        self.obj_url_handle = UrlHandle()
        # 获取基础数据
        self.base_data = self.login_data["base_variable"]



    def number_login_test(self):
        """
        执行翼课号登录的测试用例方法
        :return:
        """

        for data in  self.login_data["快速登录"]:
            # 获取url
            ori_url = data["test_case_data"]["url"]
            url = self.obj_url_handle.replace_host(ori_url=ori_url,dict_data=self.host_dict)
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            headers = data["test_case_data"]["headers"]
            print(type(data))
            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header=headers)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data])==type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    # def name_login_test(self):
    #     """
    #     执行实名登录的测试用例的方法
    #     :return:
    #     """
    #     for data in  self.login_data["实名登录"]:
    #         # 获取url
    #         url = data["test_case_data"]["url"]
    #         method = data["test_case_data"]["method"]
    #         post_data = data["test_case_data"]["data"]
    #         print(type(data))
    #         post_data = {**self.base_data,**post_data}
    #         response = self.obj_request.send_request(url=url,method=method,data=post_data)
    #         print(response.content)
    #         json_data = response.json()
    #         # 遍历用例中的期望值
    #         expected_data = data["test_case_data"]["expected"]
    #         for data in expected_data.keys():
    #             if type(expected_data[data])==type(expected_data):
    #                 for d in expected_data[data].keys():
    #                     if expected_data[data][d]==json_data[data][d]:
    #                         print("test_pass")
    #                     else:
    #                         print("test_failed")
    #             elif expected_data[data] == json_data[data]:
    #                 print("test_pass")
    #             else:
    #                 print("test_failed")


    def get_arear_test(self):
        """
        执行  获取全部地区数据列表的测试用例的 方法
        :return:
        """
        for data in  self.login_data["获取全部地区数据列表"]:
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            print(type(data))
            post_data = self.base_data
            response = self.obj_request.send_request(url=url,method=method,data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data])==type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_school_list_test(self):
        """
        执行获取学校列表的测试用例的方法
        :return:
        """
        for data in  self.login_data["获取学校列表"]:
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            print(type(data))
            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            if expected_data["status"] == json_data["status"]:
                print("test_pass")

    def search_school_test(self):
        """
        执行搜索学校的测试用例的方法
        :return:
        """
        for data in self.login_data["搜索学校"]:
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            print(type(data))
            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url, method=method, data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            if expected_data["status"] == json_data["status"]:
                print("test_pass")


    def name_login_test(self):
        """
        执行 实名登录测试用例的方法
        :return:
        """
        for data in self.login_data["实名登录"]:
            # 输出测试用例的名称
            print(data["test_case_info"]["content"])
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            print(type(data))
            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url, method=method, data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d] == json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed：" +str(expected_data[data][d]) + "==========="  + str(json_data[data][d]))
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed：" + str(expected_data[data]) + "+==================" + str(json_data[data]))

    def central_tube_scanning_code_login_test(self):
        """
        执行 央馆扫码登录的测试用例的方法
        :return:
        """
        # 首先通过辅助函数获取ticket  json_data 格式如下
        #{
          # "retCode" : "000000",
          # "data" : {
          #   "data" : "{\"retCode\":\"000000\",\"retDesc\":\"成功\",\"data\":{\"ticket\":\"OTdhNDFmNDQtZTdhNy00ZGZjLWE0MWYtNDRlN2E3M2RmYzM1MTU5NjYxMzA2MzU1MQ==\"}}"
          # }
        # }
        for data in self.login_data["央管扫码登录"]:
            # 输出测试用例的名称
            print(data["test_case_info"]["content"])
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 说明需要请求新的ticket
            if post_data["ticket_replace"] == 0:
                # 请求ticket
                json_data = self.obj_assist.get_ticket()
                if json_data["status"] == 0:
                    dict_str = json_data["data"]["data"]
                    ticket = json.loads(dict_str)["data"]["ticket"]
                    post_data["ticket"] = ticket
                    post_data.pop("ticket_replace")
                else:
                    print("获取ticket失败")
                    return json_data

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url, method=method, data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d] == json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed：" + str(expected_data[data][d]) + "===========" + str(json_data[data][d]))
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed：" + str(expected_data[data]) + "+==================" + str(json_data[data]))

    def logout_test(self,username=None,password=None):
        """
        执行 退出登录  测试用例的方法
        :param username:
        :param password:
        :return:
        """
        # 首先 获取测试用例的信息

        for data in self.login_data["退出登录"]:
            # 输出测试用例的名称
            print(data["test_case_info"]["content"])
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 预备的变量
            json_data = ""
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(username,password)
                if json_data["status"] == 0:
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                else:
                    print("用户登录失败")
                    return json_data
            if post_data["author_id_replace"] == 0:
                if json_data=="":
                    # 请求新的token
                    json_data = self.obj_assist.user_login_by_number_success(username,password)
                if json_data["status"] == 0:
                    post_data["author_id"] = json_data["data"]["uid"]
                    post_data.pop("author_id_replace")
                else:
                    print("用户登录失败")
                    return json_data

            if post_data["uid_replace"] == 0:
                if json_data == "":
                    # 请求新的token
                    json_data = self.obj_assist.user_login_by_number_success(username, password)
                if json_data["status"] == 0:
                    post_data["uid"] = json_data["data"]["uid"]
                    post_data.pop("uid_replace")
                else:
                    print("用户登录失败")
                    return json_data

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url, method=method, data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d] == json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed：" + str(expected_data[data][d]) + "===========" + str(json_data[data][d]))
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed：" + str(expected_data[data]) + "+==================" + str(json_data[data]))



# 现在配置的是线下的host
underline_host_dict = {
    "mapi.ekwing.com":"172.17.20.30"
}

online_host_dict = {}

obj_login = Login(environment="under_line",host_dict=online_host_dict)
# obj_login.number_login_test()
# obj_login.get_arear_test()
# obj_login.name_login_test()
# obj_login.central_tube_scanning_code_login_test()
obj_login.logout_test()