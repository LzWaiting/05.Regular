'''读取一个文本，分别匹配文本中所有的
* 以大写字母开头的单词（包含特殊字符的不算）
* 数字 包括整数，小数，正数，负数，分数，百分数
'''
import re

regex1 = re.compile(r'[A-Z]\w*')
regex2 = re.compile(r'-?\d+\.?/?\d*%?')

with open('test.txt') as f:
	data = f.read()

test1 = regex1.findall(data)
test2 = regex2.findall(data)
print(test1,test2,sep='\n')