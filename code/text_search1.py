import re
import sys

def get_address(cmd):
	pattern1 = r'(\d{1,3}\.){3}\d{1,3}/\d+'
	pattern2 = r'([0-9a-f]{4}\.){2}[0-9a-f]{4}'
	d = {} 
	with open('./1.txt') as f:
		phases = f.read().split('\n\n')
	for p in phases:
		one = p.split(' ')[0]
		d[one]=p
	if cmd in d and cmd != 'RP/0/RSP0/CPU0:2_c-leaf-1#':
		phase = d[cmd]
		data = re.search(pattern1,phase)
		if not data:
			IP = re.search(pattern2,phase).group()
			print(cmd,'的IP地址是',IP)
		else:
			IP = re.search(pattern1,phase).group()
			print(cmd,'的IP地址是',IP)
	elif cmd == 'RP/0/RSP0/CPU0:2_c-leaf-1#':
		print(d[cmd])
	else:
		print('输入信息不存在')

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Your argv is error')
	else:
		cmd = sys.argv[1]
		get_address(cmd)

