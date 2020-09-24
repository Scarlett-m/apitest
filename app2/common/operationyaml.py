# coding:utf8
import ruamel.yaml


class OperationYaml():
    """
    操作yaml文件的类，需要其他方法可以在这里补充
    """

    def __init__(self,file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            try:
                self.yaml_all_data = ruamel.yaml.safe_load(f)
            except ruamel.yaml.YAMLError as exc:
                print(exc)

    def get_yaml_data(self):
        return self.yaml_all_data