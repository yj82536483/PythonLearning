import re

#字符串切割
str1 = "i     love china"
print(str1.split(" "))
print(re.split(r" +",str1))

#re.finditer函数
#finditer(pattern,str,flag=0)
#返回一个迭代器
str2 = "i     love china!i     love china!i     love china!"
res = re.finditer(r"(love)",str2)
while True:
    try:
        l = next(res)
        print(l)
    except StopIteration as e:
        break


#字符串修改和替换
#re.sub(pattern, repl, string, count=0, flags=0)
#re.subn(pattern, repl, string, count=0, flags=0)
str3 = "i love love love china!"
print(re.sub(r"love","like",str3)) #返回被替换后的字符串

print(re.subn(r"love","like",str3))#返回元素，第一个元素返回替换后的字符串，第二个元素表示替换的次数


#分组





#编译
pat = r"^1(([3578]\d|(47))\d{8})$"
re_tel = re.compile(pat)




#re_QQ = re"^[1-9]\d{5,9}$"
