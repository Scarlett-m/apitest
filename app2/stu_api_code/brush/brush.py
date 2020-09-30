# coding:utf8
from app2.common.operationyaml import OperationYaml
from app2.send_request_package.send_request_moudle import optionRequest
from app2.common.assist import Assist
import json
from app2.common.urlhandle import UrlHandle

class brush:

    def __init__(self,environment,host_dict={}):
        # 读取测试用例
        self.obj_yaml = OperationYaml("../stu_api_code/brush/brush_test_case_"+environment+".yaml")
        # 获取测试用例的数据
        self.brush_data = self.obj_yaml.get_yaml_data()
        # 获取发送请求的对象
        self.obj_request = optionRequest()
        # 获取辅助的函数操作
        self.obj_assist  = Assist(environment=environment,host_dict=host_dict)
        # 获取基础数据
        self.base_data = self.brush_data["base_variable"]
        # host配置数据
        self.host_dict = host_dict
        # 获取url操作对象
        self.obj_url_handle = UrlHandle()



    def getIndexInfo_test(self,username=None,password=None):
        """
        执行智能备考首页的测试用例方法
        :param username:
        :param password:
        :return:
        """
        for data in  self.brush_data["智能备考首页"]:
            # 获取url
            url =  data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 预备的变量
            json_data = ""
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(username,password)
                # print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data])==type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            # print(expected_data[data][d])
                            print("test_pass")
                        else:
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")



    def getIndexInfo_title_middle_test(self,username=None,password=None):
        """
        执行智能备考首页初中标题测试用例方法
        :param username:
        :param password:
        :return:
        """
        for data in  self.brush_data["智能备考初中标题"]:
            # 获取url
            url =  data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 预备的变量
            json_data = ""
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(username,password)
                # print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
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

    def getIndexInfo_title_high_test(self, username=None, password=None):
                    """
                    执行智能备考首页高中标题测试用例方法
                    :param username:
                    :param password:
                    :return:
                    """
                    for data in self.brush_data["智能备考高中标题"]:
                        # 获取url
                        url = data["test_case_data"]["url"]
                        method = data["test_case_data"]["method"]
                        post_data = data["test_case_data"]["data"]

                        # 预备的变量
                        json_data = ""
                        if post_data["token_replace"] == 0:
                            # 请求新的token
                            json_data = self.obj_assist.user_login_by_number_success(username, password)
                            # print(json_data)
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
                                        # print(expected_data[data][d])
                                        print("test_pass")
                                    else:
                                        print("test_failed")
                            elif expected_data[data] == json_data[data]:
                                print("test_pass")
                            else:
                                print("test_failed")


    def dobrushsubmit_test(self, username=None, password=None):
                """
                执行智能备考智能推荐交卷测试用例方法
                :param username:
                :param password:
                :return:
                """
                for data in self.brush_data["智能推荐交卷"]:
                    # 获取url
                    url = data["test_case_data"]["url"]
                    method = data["test_case_data"]["method"]
                    post_data = data["test_case_data"]["data"]

                    # 预备的变量
                    json_data = ""
                    if post_data["token_replace"] == 0:
                        # 请求新的token
                        json_data = self.obj_assist.user_login_by_number_success(username, password)
                        # print(json_data)
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
                                    # print(json_data[data][d])
                                    # print(expected_data[data][d])
                                    print("test_failed")
                        elif expected_data[data] == json_data[data]:
                            print("test_pass")
                        else:
                            print("test_failed")


    def createBrush_test(self, username=None, password=None):
                """
                执行智能备考听说考试刷题测试用例方法
                :param username:
                :param password:
                :return:
                """
                for data in self.brush_data["听说考试刷题"]:
                    # 获取url
                    url = data["test_case_data"]["url"]
                    method = data["test_case_data"]["method"]
                    post_data = data["test_case_data"]["data"]

                    # 预备的变量
                    json_data = ""
                    if post_data["token_replace"] == 0:
                        # 请求新的token
                        json_data = self.obj_assist.user_login_by_number_success(username, password)
                        # print(json_data)
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
                    # print(post_data)

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


    def getunlist_test(self,username=None,password=None):
        """
        执行错题本列表的测试用例方法
        :param username:
        :param password:
        :return:
        """
        for data in  self.brush_data["错题本列表"]:
            # 获取url
            url =  data["test_case_data"]["url"]
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]

            # 预备的变量
            json_data = ""
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(username,password)
                # print(json_data)
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

            print(type(data))

            post_data = {**self.base_data,**post_data}
            response = self.obj_request.send_request(url=url,method=method,data=post_data)
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data])==type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            # print(expected_data[data][d])
                            print("test_pass")
                        else:
                            print("test_failed")
                            print(expected_data[data][d])
                            print(json_data[data][d])
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")




underline_host_dict = {
    "mapi.ekwing.com":"172.17.20.30"
}

online_host_dict = {}


obj_brush_api= brush(environment="online",host_dict=online_host_dict)

obj_brush_api.getIndexInfo_test(username="10278331",password="qwe123")
#运行智能备考首页测试

obj_brush_api.getIndexInfo_title_middle_test(username="10278331",password="qwe123")
#运行初中title测试

obj_brush_api.getIndexInfo_title_high_test(username="78240002",password="a666666")
#运行高中title测试


obj_brush_api.dobrushsubmit_test(username="78240002",password="a666666")
#执行智能备考提交测试

obj_brush_api.createBrush_test(username="10278331",password="qwe123")
#执行智能备考听说考试刷题测试


obj_brush_api.getunlist_test(username="10278331",password="qwe123")
# 执行错题本测试
