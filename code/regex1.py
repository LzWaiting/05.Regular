import re

# 使用finditer获取可迭代对象match
# it = re.finditer(r'\d+','2008-2019 11年，中国发生了翻天覆地的变化')
# for i in it:
# 	print(i.group())

# 使用fullmatch获取完全匹配
# try:
# 	obj = re.fullmatch(r'\w+','abcdef123')
# 	print(obj.group())
# except AttributeError as e:
# 	print(e)

# 使用match获取匹配对象
# try:
# 	obj = re.match(r'foo','foo,food on the table')
# 	print(obj.group())
# except ArithmeticError as e:
# 	print(e)

# 使用search获取第一处匹配对象
# try:
# 	obj = re.search(r'foo','Foo,food on the table')
# 	print(obj.group())
# except ArithmeticError as e:
# 	print(e)