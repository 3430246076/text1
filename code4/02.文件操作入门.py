# #读文件
# #1.打开文件
# f = open("./code3/resourse/演示文件.txt","r",encoding="utf-8")
#
# #2. 读取文件内容
# # coutent = f.read() #读取文件所有内容
# # print(coutent)
#
# countent_list = f.readlines()
# for line in countent_list:
#     print(line.strip())
# #3. 关闭文件
# f.close()


#-------------释放资源
#写文件
#1.打开文件
# f = open("./code3/resourse/静夜思.txt","w",encoding="utf-8")
#
# #2. 写入文件
# try:
#     f.write("静夜思(李白)\n\n")
#     f.write("床前明月光\n")
#     f.write("疑是地上霜\n")
#     f.write("举头望明月\n")
#     f.write("低头思故乡\n")
# finally:
#     #3. 关闭文件
#     print("文件已关闭")
#     f.close()


#=======================释放资源 方式二(最佳实践)
#1.打开文件
with open("./code3/resourse/静夜思.txt","w",encoding="utf-8") as f:
    #2. 写入文件
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")
