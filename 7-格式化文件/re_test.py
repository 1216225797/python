'''
re使用大致步骤：
1.使用compile将表示正则的字符串编译为一个pattern对象
2.通过pattern对象提供一系列方法对文本进行查找匹配，获得一个match对象，如果没有获取到，则返回None
3.最后使用match对象提供的属性和方法获得信息，根据需要进行操作


re常用函数：
group(): 获得一个或者多个分组匹配的字符串，当要获得整个匹配的子串时，直接使用group()或者group(0)
start: 获取分组匹配的子串在整个字符串中的真实位置，参数默认为0
end: 获取分组匹配的子串在整个字符串中的结果位置，默认为0
span：返回结构技术(start(group),end(group))

re修饰符
re.I 使匹配对大小写不敏感
re.L 做本地化识别（locale-aware）匹配
re.M 多行匹配，影响 ^ 和 $
re.S 使 . 匹配包括换行在内的所有字符
re.U 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

'''

import re


# c = re.compile(r'\d*')
# re.I表示忽略掉大小写
m = re.match(r'ab.*?c','abcaxc',re.I)
print(m)

# 匹配中文
# 大部分中文内容表示范围是[u4e00-u9fa5],不包括全角标点

msg = '哈哈哈dsancaonc'

f = re.findall(r'[\u4e00-\u9fa5]+',msg)
print(f)



s = "哈哈，2019-6-1 00:00:00，哦也！2019-5-24 23:59:59"

r = re.findall(r'\d{4}-\d{1}-\d{1} \d{2}:\d{2}:\d{2}',s)

print(r)