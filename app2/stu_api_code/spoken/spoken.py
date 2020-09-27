# -*- coding:utf-8 -*-
#author:Manjusaka

from app2.common.operationyaml import OperationYaml
from app2.send_request_package.send_request_moudle import optionRequest
from app2.common.assist import Assist
from app2.common.urlhandle import UrlHandle

class Spoken:
    """
    执行口语家教测试用例
    """

    def __init__(self,environment,host_dict={}):
        #读取测试用例
        self.obj_yaml = OperationYaml("../spoken/spoken_test_case_"+environment+".yaml")
        #获取测试用例的数据
        self.spoken_data = self.obj_yaml.get_yaml_data()
        #获取发送请求的对象
        self.obj_request = optionRequest()
        #获取辅助的函数操作
        self.obj_assist = Assist(environment=environment,host_dict=host_dict)
        #获取host配置字典
        self.host_dict = host_dict
        #获取操作url的对象
        self.obj_url_handle = UrlHandle()
        #获取基础数据
        self.base_data = self.spoken_data["base_variable"]

    def get_spoken_index(self, username=None, password=None):
        """
        执行获取口语家教同步主页列表数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取口语家教同步主页列表"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_index(self, username=None, password=None):
        """
        执行获取口语家教拓展主页列表数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取口语家教拓展主页列表"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_peiyin_index(self, username=None, password=None):
        """
        执行获取首页配音列表数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取首页配音列表"]:
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

    def get_book_list(self, username=None, password=None):
        """
        执行获取同步教材数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取同步教材"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_unit_list(self, username=None, password=None):
        """
        执行获取教材单元列表数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取教材单元列表"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_content(self, username=None, password=None):
        """
        执行获取同步朗读内容数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取同步朗读内容"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_video_list(self, username=None, password=None):
        """
        执行获取首页配音查看更多列表的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取首页配音查看更多列表"]:
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

    def get_album_list(self, username=None, password=None):
        """
        执行获取首页配音专辑列表数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取首页配音专辑列表"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_phonetic_index(self, username=None, password=None):
        """
        执行获取音标专练列表数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取音标专练列表"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_book_process(self, username=None, password=None):
        """
        执行获取拓展教材完成进度的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取拓展教材完成进度"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def spoken_do(self, username=None, password=None):
        """
        执行提交同步读课文内容测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["提交同步读课文内容"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_words_info(self, username=None, password=None):
        """
        执行获取课文中单词数据的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取课文中单词数据"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_peiyin_content(self, username=None, password=None):
        """
        执行获取趣味配音内容的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取趣味配音内容"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_peiyin_all(self, username=None, password=None):
        """
        执行获取趣味配音标签题目id信息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取趣味配音标签题目id信息"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_peiyin_list(self, username=None, password=None):
        """
        执行获取趣味配音列表信息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取趣味配音列表信息"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_peiyin_preview(self, username=None, password=None):
        """
        执行获取趣味配音预览信息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取趣味配音预览信息"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_other_new(self, username=None, password=None):
        """
        执行获取他人配音详情信息的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["获取他人配音详情信息"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")

    def get_spoken_share(self, username=None, password=None):
        """
        执行口语家教分享的测试用例方法
        :param username: 快速登录用户名
        :param password: 密码
        :return:
        """
        for data in self.spoken_data["口语家教分享"]:
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
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")
					
	
    def my_achieve(self):
        """
        测试我的成就
        :return:
        """

        for data in  self.other_api_data["获取url接口"]:
            # 获取url
            url = self.obj_url_handle.replace_host( ori_url=data["test_case_data"]["url"],dict_data=self.host_dict)
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            # 用户的登录翼课号：user_number
            user_number = post_data["user_number"]
            post_data.pop("user_number")

            # 用户的登录密码
            password = post_data["password"]
            post_data.pop("password")
            # 预备的变量
            json_data = ""
            # 获取token
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(user_number,password)
                if json_data["status"] == 0:
                    print(json_data)
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                    # 替换uid的值
                    post_data["uid"] = json_data["data"]["uid"]
                    # 替换author_id的值
                    post_data["author_id"] = json_data["data"]["uid"]
                else:
                    print(json_data)
                    print("用户登录失败")
                    return json_data

#             发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method, data=post_data)
#             校验接口的返回值
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


    def getspokenselflist(self):
        """
        我的成就-趣味配音列表数据
        :return:
        """

        for data in  self.other_api_data["我的成就_列表数据"]:
            # 获取url
            url = self.obj_url_handle.replace_host( ori_url=data["test_case_data"]["url"],dict_data=self.host_dict)
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            # 用户的登录翼课号：user_number
            user_number = post_data["user_number"]
            post_data.pop("user_number")

            # 用户的登录密码
            password = post_data["password"]
            post_data.pop("password")
            # 预备的变量
            json_data = ""
            # 获取token
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(user_number,password)
                if json_data["status"] == 0:
                    print(json_data)
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                    # 替换uid的值
                    post_data["uid"] = json_data["data"]["uid"]
                    # 替换author_id的值
                    post_data["author_id"] = json_data["data"]["uid"]
                else:
                    print(json_data)
                    print("用户登录失败")
                    return json_data

#             发送接口请求

            post_data = {**self.base_data, **post_data}

            #             拼接数据
            url = url + "?"
            for d in post_data:
                url = url + d + "=" + post_data[d] + "&"
            response = self.obj_request.send_request(url=url, method=method)
#             校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if type(expected_data[data][d]) == type(expected_data):
                            for dd in expected_data[data][d].keys():
                                for j in range(0,expected_data[data][d][dd].__len__()):
                                    for dd_key in expected_data[data][d][dd][j].keys():
                                        if expected_data[data][d][dd][j][dd_key] == json_data[data][d][dd][j][dd_key]:
                                            print("test_pass")
                                        else:
                                            print("test_failed")

                        elif type(expected_data[data][d]) == type([]):
                            for i in range(0,expected_data[data][d].__len__()):
                                for i_key in expected_data[data][d][i].keys():
                                    if expected_data[data][d][i][i_key] == json_data[data][d][i][i_key]:
                                        print("test_pass")
                                    else:
                                        print("test_failed")
                        elif expected_data[data][d] == json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")


    def topaward(self):
        """
        我的成就-口语之星-周榜的数据
        :return:
        """

        for data in  self.other_api_data["口语之星_周榜"]:
            # 获取url
            url = self.obj_url_handle.replace_host( ori_url=data["test_case_data"]["url"],dict_data=self.host_dict)
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            # 用户的登录翼课号：user_number
            user_number = post_data["user_number"]
            post_data.pop("user_number")

            # 用户的登录密码
            password = post_data["password"]
            post_data.pop("password")
            # 预备的变量
            json_data = ""
            # 获取token
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(user_number,password)
                if json_data["status"] == 0:
                    print(json_data)
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                    # 替换uid的值
                    post_data["uid"] = json_data["data"]["uid"]
                    # 替换author_id的值
                    post_data["author_id"] = json_data["data"]["uid"]
                else:
                    print(json_data)
                    print("用户登录失败")
                    return json_data

#             发送接口请求

            post_data = {**self.base_data, **post_data}

            #             拼接数据
            url = url + "?"
            for d in post_data:
                url = url + d + "=" + post_data[d] + "&"
            response = self.obj_request.send_request(url=url, method=method)
#             校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if type(expected_data[data][d]) == type(expected_data):
                            for dd in expected_data[data][d].keys():
                                for j in range(0,expected_data[data][d][dd].__len__()):
                                    for dd_key in expected_data[data][d][dd][j].keys():
                                        if expected_data[data][d][dd][j][dd_key] == json_data[data][d][dd][j][dd_key]:
                                            print("test_pass")
                                        else:
                                            print("test_failed")

                        elif type(expected_data[data][d]) == type([]):
                            for i in range(0,expected_data[data][d].__len__()):
                                for i_key in expected_data[data][d][i].keys():
                                    if expected_data[data][d][i][i_key] == json_data[data][d][i][i_key]:
                                        print("test_pass")
                                    else:
                                        print("test_failed")
                        elif expected_data[data][d] == json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")


    def spokenpkstar(self):
        """
        我的成就-口语之星-奖励数据
        :return:
        """

        for data in  self.other_api_data["口语之星_奖励"]:
            # 获取url
            url = self.obj_url_handle.replace_host( ori_url=data["test_case_data"]["url"],dict_data=self.host_dict)
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            # 用户的登录翼课号：user_number
            user_number = post_data["user_number"]
            post_data.pop("user_number")

            # 用户的登录密码
            password = post_data["password"]
            post_data.pop("password")
            # 预备的变量
            json_data = ""
            # 获取token
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(user_number,password)
                if json_data["status"] == 0:
                    print(json_data)
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                    # 替换uid的值
                    post_data["uid"] = json_data["data"]["uid"]
                    # 替换author_id的值
                    post_data["author_id"] = json_data["data"]["uid"]
                else:
                    print(json_data)
                    print("用户登录失败")
                    return json_data

#             发送接口请求

            post_data = {**self.base_data, **post_data}

            #             拼接数据
            url = url + "?"
            for d in post_data:
                url = url + d + "=" + post_data[d] + "&"
            response = self.obj_request.send_request(url=url, method=method)
#             校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if type(expected_data[data][d]) == type(expected_data):
                            for dd in expected_data[data][d].keys():
                                for j in range(0,expected_data[data][d][dd].__len__()):
                                    for dd_key in expected_data[data][d][dd][j].keys():
                                        if expected_data[data][d][dd][j][dd_key] == json_data[data][d][dd][j][dd_key]:
                                            print("test_pass")
                                        else:
                                            print("test_failed")

                        elif type(expected_data[data][d]) == type([]):
                            for i in range(0,expected_data[data][d].__len__()):
                                for i_key in expected_data[data][d][i].keys():
                                    if expected_data[data][d][i][i_key] == json_data[data][d][i][i_key]:
                                        print("test_pass")
                                    else:
                                        print("test_failed")
                        elif expected_data[data][d] == json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")


    def spokenstar(self):
        """
        我的成就-口语之星-奖励数据
        :return:
        """

        for data in  self.other_api_data["口语之星_总榜"]:
            # 获取url
            url = self.obj_url_handle.replace_host( ori_url=data["test_case_data"]["url"],dict_data=self.host_dict)
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            # 用户的登录翼课号：user_number
            user_number = post_data["user_number"]
            post_data.pop("user_number")

            # 用户的登录密码
            password = post_data["password"]
            post_data.pop("password")
            # 预备的变量
            json_data = ""
            # 获取token
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(user_number,password)
                if json_data["status"] == 0:
                    print(json_data)
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                    # 替换uid的值
                    post_data["uid"] = json_data["data"]["uid"]
                    # 替换author_id的值
                    post_data["author_id"] = json_data["data"]["uid"]
                else:
                    print(json_data)
                    print("用户登录失败")
                    return json_data

#             发送接口请求

            post_data = {**self.base_data, **post_data}

            #             拼接数据
            url = url + "?"
            for d in post_data:
                url = url + d + "=" + post_data[d] + "&"
            response = self.obj_request.send_request(url=url, method=method)
#             校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if type(expected_data[data][d]) == type(expected_data):
                            for dd in expected_data[data][d].keys():
                                for j in range(0,expected_data[data][d][dd].__len__()):
                                    for dd_key in expected_data[data][d][dd][j].keys():
                                        if expected_data[data][d][dd][j][dd_key] == json_data[data][d][dd][j][dd_key]:
                                            print("test_pass")
                                        else:
                                            print("test_failed")

                        elif type(expected_data[data][d]) == type([]):
                            for i in range(0,expected_data[data][d].__len__()):
                                for i_key in expected_data[data][d][i].keys():
                                    if expected_data[data][d][i][i_key] == json_data[data][d][i][i_key]:
                                        print("test_pass")
                                    else:
                                        print("test_failed")
                        elif expected_data[data][d] == json_data[data][d]:
                            print("test_pass")
                        else:
                            print("test_failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")


    def pkarenas(self):
        """
        测试我的pk数据和我的对手列表
        :return:
        """

        for data in  self.other_api_data["pk竞技场_获取用户的pk数据"]:
            # 获取url
            url = self.obj_url_handle.replace_host( ori_url=data["test_case_data"]["url"],dict_data=self.host_dict)
            method = data["test_case_data"]["method"]
            post_data = data["test_case_data"]["data"]
            # 用户的登录翼课号：user_number
            user_number = post_data["user_number"]
            post_data.pop("user_number")

            # 用户的登录密码
            password = post_data["password"]
            post_data.pop("password")
            # 预备的变量
            json_data = ""
            # 获取token
            if post_data["token_replace"] == 0:
                # 请求新的token
                json_data = self.obj_assist.user_login_by_number_success(user_number,password)
                if json_data["status"] == 0:
                    print(json_data)
                    post_data["token"] = json_data["data"]["token"]
                    post_data.pop("token_replace")
                    # 替换uid的值
                    post_data["uid"] = json_data["data"]["uid"]
                    # 替换author_id的值
                    post_data["author_id"] = json_data["data"]["uid"]
                else:
                    print(json_data)
                    print("用户登录失败")
                    return json_data

#             发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method, data=post_data)
#             校验接口的返回值
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



host_dict = {
    "mapi.ekwing.com":"172.17.20.30"
}

#线上环境
obj_usercenter_api = Spoken(environment="online")

#执行获取口语家教同步主页列表数据的测试用例
obj_usercenter_api.get_spoken_index(username="10279464", password="qwe123")
#执行获取口语家教拓展主页列表数据的测试用例
obj_usercenter_api.get_index(username="10279128", password="qwe123")
#执行获取首页配音列表数据的测试用例
obj_usercenter_api.get_peiyin_index(username="10279464", password="qwe123")
#执行获取同步教材数据的测试用例
obj_usercenter_api.get_book_list(username="10279464", password="qwe123")
#执行获取教材单元列表数据的测试用例
obj_usercenter_api.get_unit_list(username="10279128", password="qwe123")
#执行获取同步朗读内容的测试用例
obj_usercenter_api.get_content(username="10279464", password="qwe123")
#执行获取首页配音查看更多列表数据的测试用例
obj_usercenter_api.get_video_list(username="10279464", password="qwe123")
#执行获取首页配音专辑表数据的测试用例
obj_usercenter_api.get_album_list(username="10279464", password="qwe123")
#执行获取音标专练列表数据的测试用例
obj_usercenter_api.get_phonetic_index(username="10279464", password="qwe123")
#执行获取拓展教材完成进度的测试用例-仅iOS
obj_usercenter_api.get_book_process(username="10279464", password="qwe123")
#执行提交同步读课文内容的测试用例
obj_usercenter_api.spoken_do(username="10279464", password="qwe123")
#执行获取课文中单词数据的测试用例
obj_usercenter_api.get_book_process(username="10279464", password="qwe123")
#执行获取趣味配音内容的测试用例
obj_usercenter_api.get_peiyin_content(username="10279464", password="qwe123")
#执行获取趣味配音标签题目id信息的测试用例
obj_usercenter_api.get_peiyin_all(username="10279464", password="qwe123")
#执行获取趣味配音列表信息的测试用例
obj_usercenter_api.get_peiyin_list(username="10279464", password="qwe123")
#执行获取趣味配音预览信息的测试用例
obj_usercenter_api.get_peiyin_preview(username="10279464", password="qwe123")
#执行获取他人配音详情信息的测试用例
obj_usercenter_api.get_other_new(username="10279464", password="qwe123")
#执行口语家教分享的测试用例
obj_usercenter_api.get_spoken_share(username="10279464", password="qwe123")


# 线下环境
obj_usercenter_api_underline = Spoken(environment="under_line",host_dict=host_dict)

#执行获取口语家教同步主页列表数据的测试用例
obj_usercenter_api_underline.get_spoken_index(username="10278719", password="666666")
#执行获取口语家教拓展主页列表数据的测试用例
obj_usercenter_api_underline.get_index(username="10278719", password="666666")
#执行获取首页配音列表数据的测试用例
obj_usercenter_api_underline.get_peiyin_index(username="10278719", password="666666")
#执行获取同步教材数据的测试用例
obj_usercenter_api_underline.get_book_list(username="10278719", password="666666")
#执行获取教材单元列表数据的测试用例
obj_usercenter_api_underline.get_unit_list(username="10278719", password="666666")
#执行获取同步朗读内容的测试用例
obj_usercenter_api_underline.get_content(username="10278719", password="666666")
#执行获取首页配音查看更多列表数据的测试用例
obj_usercenter_api_underline.get_video_list(username="10278719", password="666666")
#执行获取首页配音专辑表数据的测试用例
obj_usercenter_api_underline.get_album_list(username="10278719", password="666666")
#执行获取音标专练列表数据的测试用例
obj_usercenter_api_underline.get_phonetic_index(username="10278719", password="666666")
#执行获取拓展教材完成进度的测试用例-仅iOS
obj_usercenter_api_underline.get_book_process(username="10278719", password="666666")
#执行提交同步读课文内容的测试用例
obj_usercenter_api_underline.spoken_do(username="10278719", password="666666")
#执行获取课文中单词数据的测试用例
obj_usercenter_api_underline.get_book_process(username="10278719", password="666666")
#执行获取趣味配音内容的测试用例
obj_usercenter_api.get_peiyin_content(username="10278719", password="666666")
#执行获取趣味配音标签题目id信息的测试用例
obj_usercenter_api.get_peiyin_all(username="10278719", password="666666")
#执行获取趣味配音列表信息的测试用例
obj_usercenter_api.get_peiyin_list(username="10278719", password="666666")
#执行获取趣味配音预览信息的测试用例
obj_usercenter_api.get_peiyin_preview(username="10278719", password="666666")
#执行获取他人配音详情信息的测试用例
obj_usercenter_api.get_other_new(username="10278719", password="666666")
#执行口语家教分享的测试用例
obj_usercenter_api.get_spoken_share(username="10278719", password="666666")


# obj_ekspeaking = EkSpeaking(environment="online",host_dict=host_dict)
# # obj_ekspeaking.my_achieve()
# # obj_ekspeaking.getspokenselflist()
# # obj_ekspeaking.topaward()
# # obj_ekspeaking.spokenstar()
#
# # obj_ekspeaking.spokenpkstar()
# obj_ekspeaking.pkarenas()