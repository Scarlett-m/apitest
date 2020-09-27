# coding:utf8

class UrlHandle():

    """
    主要是用来操作url的，用来控制这个接口访问的是哪个服务器
    """
    {
        "mapi.ekwig.com":"172.17...."
    }
    def replace_host(self,ori_url,dict_data={}):
        aim_url = ori_url
        for key in dict_data.keys():
            if key in  ori_url:
                aim_url = ori_url.replace(key,dict_data[key])


        return aim_url

    pass



