# coding:utf8
from app2.stu_api_code.common.operationyaml import OperationYaml
from app2.stu_api_code.send_request_package.send_request_moudle import optionRequest
from app2.stu_api_code.common.assist import Assist
from app2.stu_api_code.common.urlhandle import UrlHandle

class EkCollege():
    """
    翼课学院相关接口的测试用例的方法
    返回页面的不先不写



    """

    def __init__(self,environment,host_dict={}):
        # 读取测试用例
        self.obj_yaml = OperationYaml("../ekcollege/ek_college_test_case_"+environment+".yaml")
        # 获取测试用例的数据
        self.other_api_data = self.obj_yaml.get_yaml_data()
        # 获取发送请求的对象
        self.obj_request = optionRequest()
        # 获取辅助的函数操作
        self.obj_assist  = Assist(environment=environment,host_dict=host_dict)
        # 获取基础数据
        self.base_data = self.other_api_data["base_variable"]
        # host配置数据
        self.host_dict = host_dict
        # 获取url操作对象
        self.obj_url_handle = UrlHandle()

    def doselfstudy_test(self):
        """
        测试用户的自学情况的用例
        :return:
        """

        for data in  self.other_api_data["用户自学情况"]:
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


    def getcollegeindex_test(self):
        """
        翼课学院首页数据的用例
        :return:
        """

        for data in  self.other_api_data["翼课学院首页初始数据"]:
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


    def gettasklist_test(self):
        """
        翼课学院首页任务列表的用例
        :return:
        """

        for data in  self.other_api_data["翼课学院任务列表"]:
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
                # 如果是字典
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        # 如果还是字典
                        if type(expected_data[data][d]) == type(expected_data):
                            for dd in expected_data[data][d].keys():
                               if expected_data[data][d][dd] == json_data[data][d][dd]:
                                   print("test_pass")
                               else:
                                   print("test_pass")

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


    def college_toh5(self):
        """
        https://mapi.ekwing.com/student/college/toh5
        :return:
        """

        for data in  self.other_api_data["https://mapi.ekwing.com/student/college/toh5"]:
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


    def college_rememberbook(self):
        """
        https://mapi.ekwing.com/student/college/toh5
        :return:
        """

        for data in self.other_api_data["单词向前冲-修改教材信息"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            # 给url拼接其他参数
            url = url + "?"
            for key in post_data.keys():
                url=url+ key + "=" + str(post_data[key]) + "&"

            response = self.obj_request.send_request(url=url, method=method)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    print("test_failed")


    def college_getwordtoll(self):
        """
        https://mapi.ekwing.com/student/college/getwordtoll
        :return:
        """

        for data in self.other_api_data["单词向前冲-关卡列表信息"]:
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

            # 发送修改教材的请求
            # book_info:{"status":"0","data":{"book_name":"书本名称"}}
            book_info = self.obj_assist.college_remember_book(uid=post_data["uid"],token=post_data["token"])
            if book_info["status"]=="1":
                print(book_info["msg"])
                return False
            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            # 拼接url
            url = url + "?"
            for key in post_data.keys():
                url = url + key + "=" + str(post_data[key]) +"&"
            response = self.obj_request.send_request(url=url, method=method)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            expected_data["data"]["book"] = book_info["data"]["book_name"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")


    def college_dotoll(self):
        """
        https://mapi.ekwing.com/student/college/getwordtoll
        :return:
        """

        for data in self.other_api_data["单词向前冲给-提交结果"]:
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
            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")


    def college_getpointinfo(self):
        """
        词汇记忆获取关卡列表
        https://mapi.ekwing.com/student/college/getwordtoll
        :return:
        """

        for data in self.other_api_data["专项练一练-关卡列表"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif type(expected_data[data]) == type([]):
                    for i in range(0,expected_data[data].__len__()):
                        for d in expected_data[data][i].keys():
                            if expected_data[data][i][d] == json_data[data][i][d]:
                                print("test_pass")
                            else:
                                print("test_faild")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")

    def college_savepoints(self):
        """
        词汇记忆提交测验
        https://mapi.ekwing.com/student/college/savepoints
        :return:
        """

        for data in self.other_api_data["词汇记忆-提交测验数据"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif type(expected_data[data]) == type([]):
                    for i in range(0,expected_data[data].__len__()):
                        for d in expected_data[data][i].keys():
                            if expected_data[data][i][d] == json_data[data][i][d]:
                                print("test_pass")
                            else:
                                print("test_faild")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")

    def college_maplist(self):
        """
        同步阅读获取地图列表
        :return:
        """

        for data in self.other_api_data["专项练一练-地图列表"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")


    def college_getpointdata(self):
        """
        词汇记忆 获取测验的数据
        :return:
        """

        for data in self.other_api_data["词汇记忆-测验数据"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")

    def college_getcgread(self):
        """
        同步阅读 获取测验的数据
        :return:
        """

        for data in self.other_api_data["同步阅读-测验数据"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")

    def college_submitcgread(self):
        """
        同步阅读 提交测验的数据
        :return:
        """

        for data in self.other_api_data["同步阅读-提交测验数据"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")

    def college_gettextbyids(self):
        """
        连词成句 获取测验的数据
        :return:
        """
        for data in self.other_api_data["连词成句-测验数据"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")

    def college_submitWordsentence(self):
        """
        连词成句 提交测验的数据
        :return:
        """

        for data in self.other_api_data["连词成句-提交测验数据"]:
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

            # 发送接口请求
            post_data = {**self.base_data, **post_data}
            response = self.obj_request.send_request(url=url, method=method,data=post_data)
            # 校验接口的返回值
            print(response.content)
            json_data = response.json()
            # 遍历用例中的期望值
            expected_data = data["test_case_data"]["expected"]
            for data in expected_data.keys():
                if type(expected_data[data]) == type(expected_data):
                    for d in expected_data[data].keys():
                        if expected_data[data][d]==json_data[data][d]:
                            print("test pass")
                        else:
                            print("test failed")
                elif expected_data[data] == json_data[data]:
                    print("test_pass")
                else:
                    if data=="status":
                        print("接口报错")
                        return False
                    print("test_failed")


host_dict = {
    # "mapi.ekwing.com":"172.17.20.30"
}


# obj_ekcollege = EkCollege(environment="online",host_dict=host_dict)
# # obj_ekcollege.doselfstudy_test()
# # obj_ekcollege.getcollegeindex_test()
# # obj_ekcollege.gettasklist_test()
# # obj_ekcollege.college_toh5()
# # obj_ekcollege.college_rememberbook()
# # obj_ekcollege.college_getwordtoll()
# # obj_ekcollege.college_dotoll()
# # obj_ekcollege.college_getpointinfo()
# # obj_ekcollege.college_maplist()
# # obj_ekcollege.college_getpointdata()
# # obj_ekcollege.college_getcgread()
# # obj_ekcollege.college_gettextbyids()
# # obj_ekcollege.college_submitWordsentence()
# # obj_ekcollege.college_submitcgread()
# obj_ekcollege.college_savepoints()
