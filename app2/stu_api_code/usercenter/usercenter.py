# -*- coding:utf-8 -*-

from app2.stu_api_code.common.operationyaml import OperationYaml
from app2.stu_api_code.send_request_package.send_request_moudle import optionRequest
from app2.stu_api_code.common.assist import Assist
from app2.stu_api_code.common.urlhandle import UrlHandle

class UserCenter:
    """
    执行个人中心的测试用例
    """

    def __init__(self,environment,host_dict={}):
        #读取测试用例
        self.obj_yaml = OperationYaml("../usercenter/usercenter_test_case_"+environment+".yaml")
        #获取测试用例的数据
        self.usercenter_data = self.obj_yaml.get_yaml_data()
        #获取发送请求的对象
        self.obj_request = optionRequest()
        #获取辅助的函数操作
        self.obj_assist = Assist(environment=environment,host_dict=host_dict)
        #获取host配置字典
        self.host_dict = host_dict
        #获取操作url的对象
        self.obj_url_handle = UrlHandle()
        #获取基础数据
        self.base_data = self.usercenter_data["base_variable"]

    def get_msgcenter_list_test(self,username=None,password=None):
        """
        执行获取我的消息未读消息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.usercenter_data["获取我的消息未读消息数"]:
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 预备的变量
            json_data = ""
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(username, password)
                if json_data["status"] == 0:
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                else:
                    print("用户登录失败")
                    return json_data
            if post_data["author_id_replace"] == 0:
                if json_data == "":
                    # 请求新的token
                    json_data = self.obj_assist.user_login_by_number_success(username, password)
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

            print(type(data))

            post_data = {**self.base_data, **post_data}
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
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")
    def get_msg_list_test(self,username=None,password=None):
        """
        执行获取系统消息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.usercenter_data["获取系统消息"]:
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 预备的变量
            json_data = ""
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(username, password)
                if json_data["status"] == 0:
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                else:
                    print("用户登录失败")
                    return json_data
            if post_data["author_id_replace"] == 0:
                if json_data == "":
                    # 请求新的token
                    json_data = self.obj_assist.user_login_by_number_success(username, password)
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

            print(type(data))

            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method, data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            print(data["test_case_data"]["expected"])
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d] == json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_study_msg_list_test(self,username=None,password=None):
        """
        执行获取学习消息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.usercenter_data["获取学习消息"]:
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 预备的变量
            json_data = ""
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(username, password)
                if json_data["status"] == 0:
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                else:
                    print("用户登录失败")
                    return json_data
            if post_data["author_id_replace"] == 0:
                if json_data == "":
                    # 请求新的token
                    json_data = self.obj_assist.user_login_by_number_success(username, password)
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

            print(type(data))

            post_data = {**self.base_data, **post_data}
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
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_pk_msg_list_test(self,username=None,password=None):
        """
        执行获取pk消息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.usercenter_data["获取pk消息"]:
            # 获取url
            url = data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 预备的变量
            json_data = ""
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(username, password)
                if json_data["status"] == 0:
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                else:
                    print("用户登录失败")
                    return json_data
            if post_data["author_id_replace"] == 0:
                if json_data == "":
                    # 请求新的token
                    json_data = self.obj_assist.user_login_by_number_success(username, password)
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

            print(type(data))

            post_data = {**self.base_data, **post_data}
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
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_user_vip_info(self,username=None,password=None):
        """
        执行获取vip用户详细信息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in  self.usercenter_data["获取vip用户详细信息"]:
            # 获取url
            url = self.obj_url_handle.replace_host( ori_url=data["test_case_data"]["url"],dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            # for data in expected_data.keys():
            #     if type(expected_data[data]) == type(expected_data):
            #         for d in expected_data[data].keys():
            #             try:
            #                 if expected_data[data][d] == json_data[data][d]:
            #                     print("test_pass")
            #                 else:
            #                     print("test_failed")
            #             except KeyError:
            #                 pass
            #     elif expected_data[data] == json_data[data]:
            #         print("test_pass")
            #     else:
            #         print("test_failed")
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

    def get_user_nonvip_info(self,username=None,password=None):
        """
        执行获取非vip用户详细信息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in  self.usercenter_data["获取非vip用户详细信息"]:
            # 获取url
            url = self.obj_url_handle.replace_host( ori_url=data["test_case_data"]["url"],dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        try:
                            if expected_data[data][d] == json_data[data][d]:
                                print("test_pass")
                            else:
                                print("test_failed")
                        except KeyError:
                            pass
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_user_cloud_info(self,username=None,password=None):
        """
        执行获取云会员详细信息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in  self.usercenter_data["获取云会员用户详细信息"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url, method=method, data=post_data,header={"Host":"mapi.ekwing.com"})
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        try:
                            if type(expected_data[data][d]) == type(json_data[data][d]):
                                for m in expected_data[data][d].keys():
                                    if expected_data[data][d][m] == json_data[data][d][m]:
                                        print("test_pass")
                                    else:
                                        print("test_failed")
                            elif expected_data[data][d] == json_data[data][d]:
                                print("test_pass")
                            else:
                                print("test_failed")
                        except KeyError:
                            pass
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_class_new_dynamic_num(self,username=None,password=None):
        """
        执行获取班级动态新消息数的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in  self.usercenter_data["获取班级动态新消息数"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
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

    def get_dynamic_list(self,username=None,password=None):
        """
        执行获取班级动态列表的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in  self.usercenter_data["获取班级动态"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def user_like(self,username=None,password=None):
        """
        执行全局点赞的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in  self.usercenter_data["全局点赞"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_level_conf(self, username=None, password=None):
        for data in  self.usercenter_data["获取等级详细信息"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
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

    def get_bind_list(self, username=None, password=None):
        for data in  self.usercenter_data["获取绑定家长信息"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
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

    def get_class_list(self, username=None, password=None):
        for data in  self.usercenter_data["获取学生全部班级信息"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
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

    def get_search_class(self, username=None, password=None):
        for data in  self.usercenter_data["学生输入班级号搜索班级"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
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

    def get_expand_index(self, username=None, password=None):
        for data in  self.usercenter_data["学生环保值首页"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
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

    def get_expand_rank(self, username=None, password=None):
        for data in  self.usercenter_data["学生环保值排行榜"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_expand_honor(self, username=None, password=None):
        for data in  self.usercenter_data["学生环保值证书"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
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

    def get_expand_detail(self, username=None, password=None):
        for data in  self.usercenter_data["学生环保值历史"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_expand_module(self, username=None, password=None):
        for data in  self.usercenter_data["学生环保值模块信息"]:
            # 获取url
            url = self.obj_url_handle.replace_host(ori_url=data["test_case_data"]["url"], dict_data=self.host_dict)
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
                    print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data,header={"Host":"mapi.ekwing.com"})
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

host_dict = {
    "mapi.ekwing.com":"172.17.20.30"
}

#线上环境

obj_usercenter_api = UserCenter(environment="online")
#执行获取我的消息未读消息的测试用例
obj_usercenter_api.get_msgcenter_list_test(username="10279464",password="qwe123")
#执行获取系统消息列表的测试用例
obj_usercenter_api.get_msg_list_test(username="10279464", password="qwe123")
#执行获取学习消息列表的测试用例
obj_usercenter_api.get_study_msg_list_test(username="10279128",password="qwe123")
#执行获取pk消息列表的测试用例
obj_usercenter_api.get_pk_msg_list_test(username="10279464",password="qwe123")
#执行获取vip用户权限信息的测试用例
obj_usercenter_api.get_user_vip_info(username="10279128", password="qwe123")
#执行获取非vip用户权限信息的测试用例
obj_usercenter_api.get_user_nonvip_info(username="10279381", password="a123123")
#执行获取云会员用户信息的测试用例
obj_usercenter_api.get_user_cloud_info(username="1775900187", password="666666")
#执行获取班级动态新消息数的测试用例
obj_usercenter_api.get_class_new_dynamic_num(username="10279464", password="qwe123")
#执行获取班级动态列表的测试用例
obj_usercenter_api.get_dynamic_list(username="10279128", password="qwe123")
#执行全局点赞的测试用例
obj_usercenter_api.user_like(username="10279464", password="qwe123")
#执行获取等级详细信息数的测试用例
obj_usercenter_api.get_level_conf(username="10279128", password="qwe123")
#执行获取绑定家长信息的测试用例
#需要使用已绑定家长的学生账号
obj_usercenter_api.get_bind_list(username="10279464", password="qwe123")
#执行获取学生全部班级信息的测试用例
obj_usercenter_api.get_class_list(username="10279464", password="qwe123")
#执行学生输入班级号搜索班级的测试用例
#输入一个励志学校下的学生账号
obj_usercenter_api.get_search_class(username="10279128", password="qwe123")
#执行获取学生环保值首页的测试用例
#输入一个C端学生账号
obj_usercenter_api.get_expand_index(username="10279464", password="qwe123")
#执行获取学生环保值排行榜的测试用例
#输入一个C端学生账号
obj_usercenter_api.get_expand_rank(username="10279464", password="qwe123")
#执行获取学生环保值证书的测试用例
#输入一个C端学生账号
obj_usercenter_api.get_expand_honor(username="10279128", password="qwe123")
#执行获取学生环保历史的测试用例
#输入一个C端学生账号
obj_usercenter_api.get_expand_detail(username="10279464", password="qwe123")
#执行获取学生环保值模块信息的测试用例
#输入一个C端学生账号
obj_usercenter_api.get_expand_module(username="10279128", password="qwe123")


#线下环境
obj_usercenter_api_underline = UserCenter(environment="under_line",host_dict=host_dict)
#执行获取我的消息未读消息的测试用例
obj_usercenter_api_underline.get_msgcenter_list_test(username="10278719",password="666666")
#执行获取系统消息列表的测试用例
obj_usercenter_api_underline.get_msg_list_test(username="10278719",password="666666")
#执行获取学习消息列表的测试用例
obj_usercenter_api_underline.get_study_msg_list_test(username="10278719",password="666666")
#执行获取pk消息列表的测试用例
obj_usercenter_api_underline.get_pk_msg_list_test(username="10278719",password="666666")
#执行获取vip用户权限信息的测试用例
obj_usercenter_api_underline.get_user_vip_info(username="10278719",password="666666")
#执行获取非vip用户权限信息的测试用例
obj_usercenter_api_underline.get_user_nonvip_info(username="12714877", password="666666")
#执行获取云会员用户信息的测试用例
obj_usercenter_api_underline.get_user_cloud_info(username="1902900003", password="666666")
#执行获取班级动态新消息数的测试用例
obj_usercenter_api_underline.get_class_new_dynamic_num(username="10278719",password="666666")
#执行获取班级动态列表的测试用例
obj_usercenter_api.get_dynamic_list(username="10278719", password="666666")
#执行全局点赞的测试用例
obj_usercenter_api.user_like(username="10278719", password="666666")
#执行获取等级详细信息数的测试用例
obj_usercenter_api_underline.get_level_conf(username="10278719",password="666666")
#执行获取绑定家长信息的测试用例
#需要使用已绑定家长的学生账号
obj_usercenter_api_underline.get_bind_list(username="10278719",password="666666")
#执行获取学生全部班级信息的测试用例
obj_usercenter_api_underline.get_class_list(username="10278719",password="666666")
#执行学生输入班级号搜索班级的测试用例
#输入一个励志学校下的学生账号
obj_usercenter_api_underline.get_search_class(username="10278719",password="666666")
#执行获取学生环保值首页的测试用例
#输入一个C端学生账号
obj_usercenter_api_underline.get_expand_index(username="10278719",password="666666")
#执行获取学生环保值排行榜的测试用例
#输入一个C端学生账号
obj_usercenter_api_underline.get_expand_rank(username="10278719",password="666666")
#执行获取学生环保值证书的测试用例
#输入一个C端学生账号
obj_usercenter_api_underline.get_expand_honor(username="10278719",password="666666")
#执行获取学生环保历史的测试用例
#输入一个C端学生账号
obj_usercenter_api_underline.get_expand_detail(username="10278719",password="666666")
#执行获取学生环保值模块信息的测试用例
#输入一个C端学生账号
obj_usercenter_api_underline.get_expand_module(username="10278719",password="666666")


