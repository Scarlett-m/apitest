# coding:utf8
from app2.stu_api_code.ekspeaking.ek_speaking import EkSpeaking
from app2.stu_api_code.common.operationyaml import OperationYaml
from app2.stu_api_code.send_request_package.send_request_moudle import optionRequest
from app2.stu_api_code.common.assist import Assist
from app2.stu_api_code.common.urlhandle import UrlHandle

class OtherApi:

    def __init__(self,environment,host_dict={}):
        # 读取测试用例
        self.obj_yaml = OperationYaml("../other_api/other_api_test_case_"+environment+".yaml")
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



    def get_all_config(self,username=None,password=None):
        """

        :param username:
        :param password:
        :return:
        """
        for data in  self.other_api_data["获取全局配置信息"]:
            # 获取url
            url =  data["test_case_data"]["url"]
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


    def get_user_info(self,username=None,password=None):
        for data in  self.other_api_data["获取用户基本信息"]:
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


host_dict = {
    "mapi.ekwing.com":"172.17.20.30"
}

# obj_other_api = OtherApi(environment="under_line",host_dict=host_dict)
# # obj_other_api.get_all_config()
# obj_other_api.get_user_info(username="10278314",password="666666")