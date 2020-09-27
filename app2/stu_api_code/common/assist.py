# coding:utf8
from app2.send_request_package.send_request_moudle import optionRequest
from app2.common.operationyaml import OperationYaml
import hashlib
from app2.common.urlhandle import UrlHandle



class Assist():

    """
    辅助测试类，主要获取测试用例中需要用到的的数据的接口请求
    """

    def __init__(self,environment,host_dict):
        """

        :param environment: online,under_line  运行这个接口的环境
        """
        # request的请求对象
        self.obj_op_requ = optionRequest()
        # 操作yaml的操作对象
        self.obj_op_yaml = OperationYaml("../common/assist_"+environment+".yaml")
        # yaml的数据
        self.assist_data = self.obj_op_yaml.get_yaml_data()
        # 测试用例接口的基础数据
        self.base_data = self.assist_data["base_variable"]
        # url的操作方法
        self.obj_url_handle = UrlHandle()
        # host配置字典
        self.host_data = host_dict

    def get_ticket(self):
        """
        获取央管的ticket
        :return: 返回接口返回的数据
        """

        data = self.assist_data["获取央管ticket"]
        url = data["url"]
        method = data["method"]
        post_data = data["data"]
        try:
            json_data = self.obj_op_requ.send_request(url=url,method=method,data=post_data).json()
            json_data["status"] = 0
        except:
            print("获取ticket失败")
            json_data ={
                "status":1,
                "msg":"获取ticket失败"
            }
        return json_data

    def user_login_by_number_success(self,username=None,password=None):
        """
        翼课号登录方法
        :param username: 输入登录的学生翼课号
        :param password: 输入登录的学生密码  程序进行md5加密
        :return: 返回登录的json数据
        """

        data = self.assist_data["翼课号登录"]
        url = self.obj_url_handle.replace_host(ori_url= data["url"],dict_data=self.host_data)
        method = data["method"]
        post_data = data["data"]
        headers = data["header"]
        if username!=None:
            post_data["username"] = username
        if password != None:
            # 对密码进行md5加密
            password = hashlib.md5(password.encode())
            post_data["password"] = password.hexdigest()
        try:
            post_data = {**self.base_data,**post_data}
            json_data = self.obj_op_requ.send_request(url=url,method=method,data=post_data,header=headers).json()
        except:
            print("用户登录失败")
            json_data ={
                "status": 1,
                "msg":"用户登录失败"
            }
        return json_data

host_dict = {
    "mapi.ekwing.com":"172.17.20.30"
    }

obj_assist = Assist(environment='under_line',host_dict=host_dict)
data = obj_assist.user_login_by_number_success()
print(data)