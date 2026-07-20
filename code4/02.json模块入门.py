import json

#导入json数据文件
user = {
    "name": "泡芙",
    "age": 18,
    "nature":  "温柔可爱的台湾妹子"
}
with open("resourse/user.json","w",encoding="utf-8") as f:
    #ensure_ascii:默认为true,确保所有的数据都是asicc编码(带ASCII码会进行转义);False,带ASCII码保留原样输出
    #indent:会在输出的json数据中添加缩进(格式化)

    json.dump(user,f,ensure_ascii=False,indent=2)

#读取json数据文件
with open("resourse/user.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))