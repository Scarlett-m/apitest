# -*- coding:utf-8 -*-
#author:Manjusaka

# data = {
#     "name": "xiaoming",
#     "sex": True,
#     "age": 18
# }
#
# test = {
#     "name": "xiaohua",
#     "sex": True,
# }
#
# for a in data.keys():
#     for b in test.keys():
#         if a==b:
#             if data[a]==test[b]:
#                 print("yes")
#         else:
#             pass




json_data = {
    "data":{
        "name": "xiaohua",
        "class":{
            "school": 1
        }
    },
    "status": 0
}


# 遍历用例中的期望值
expected_data = {
    "data":{
        "name": "xiaohua",
        "age": 18,
        "class":{
            "school": 1
        }
    },
    "status": 0
}
for data in expected_data.keys():
    if type(expected_data[data])==type(expected_data):
        for d in expected_data[data].keys():
            try:
                if expected_data[data][d]==json_data[data][d]:
                    print("test_pass")
                else:
                    print("test_failed")
            except KeyError:
                pass
    elif expected_data[data] == json_data[data]:
        print("test_pass1")
    else:
        print("test_failed1")

# for data in expected_data.keys():
#     if expected_data[data] == json_data[data]:
#         print("test_pass")
#     else:
#         print("test_failed")