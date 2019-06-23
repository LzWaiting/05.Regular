import re

pattern = r'(ab)c(de)f'
s = 'abcdefghigklmnabcdef'

# re模块直接调用
# l = re.findall(pattern,s)

# compile对象方法调用
# regex = re.compile(pattern)
# l = regex.findall(s)	# [('ab', 'de'), ('ab', 'de')]

# 使用split切割字符串
# l = re.split(r'\s+','Hello world   nihao China')	# ['Hello', 'world', 'nihao', 'China']

# 使用sub替换字符串
# s1 = re.sub(r'\s+','#','Hello world   nihao China')			# Hello#world#nihao#China
# t = re.subn(r'\s+','#','Hello world   nihao China',2)		# ('Hello#world#nihao China', 2)

print(s1)