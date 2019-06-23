import re

s = '''hello world
hello Kitty
你好，成都'''

pattern = r'^你好'

regex = re.compile(pattern,flags=re.M)

try:
	data = regex.search(s).group()
except:
	print('没有匹配到内容')
else:
	print(data)