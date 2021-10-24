# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/23
import json


class Contact:
    def __init__(self, first, last, **kwarg):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


c = Contact("John", "Smith")
print(c.__dict__)
json.dumps(c.__dict__)

print("缺少了full_name的屬性可以讓使用者看見。")


print('-'*36)
print("""自訂編碼程序來完成。""")


class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return dict(
                first=obj.first,
                last=obj.last,
                full=obj.full_name,
                is_contact=True
            )
        return super().default(obj)


c_e = json.dumps(c, cls=ContactEncoder)
print(c_e)

print('-'*36)
print("""也可以自訂解碼流程。 並非所有讀到的資訊都要接收。""")


def decode_contact(dic):
    if dic.get("is_contact"):
        return Contact(**dic)
    return dic


c_d = json.loads(c_e, object_hook=decode_contact)
print(c_d.__dict__)
