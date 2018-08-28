import json
test = input("请输入你的text:")
print(test)
def foo(obj):
    return {
        "name":"name"
    }

r = json.dumps(test,default=foo)
print(type(r))


