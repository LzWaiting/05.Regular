import re

pattern = r'(?P<letter1>ab)cd(?P<letter2>ef)'
regex = re.compile(pattern)

match_obj = regex.search('abcdefghijklmnopqrstuvwxyz')

print(match_obj.pos) 		# 匹配目标字符串的开始位置
print(match_obj.endpos)  	# 匹配目标字符串的结束位置
print(match_obj.re)  		# 正则表达式
print(match_obj.string)  	# 目标字符串
print(match_obj.lastgroup)	# 最后一组的组名
print(match_obj.lastindex)	# 最后一组是第几组

print(match_obj.start())	# 匹配内容的开始位置
print(match_obj.end())		# 匹配内容的结束位置
print(match_obj.span())		# 匹配内容的起止位置
print(match_obj.group())	# 获取整个match 对象对应的内容
print(match_obj.groupdict())# 获取捕获组名作为键，对应内容为值的字典
print(match_obj.groups())	# 获取每个子组匹配内容