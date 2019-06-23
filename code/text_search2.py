import re
import sys

def get_address(cmd):
	pattern = r'\S+'
	pattern1 = r'address is (\d{1,3}\.){3}\d{1,3}/\d+|Unknown'
	# pattern2 = r'address is ([0-9a-f]{4}\.){2}[0-9a-f]{4}'
	pattern2 = r'address is (\w{4}\.\w{4}\.\w{4})'
	with open('./1.txt') as f:
		while True:	
			data = ''
			for line in f:
				if line != '\n':
					data += line
				else:
					break
			if not data:
				return 'Not Found the port'
			try:
				CMD = re.match(pattern,data).group()
			except Exception as e:
				print(e)
				continue
			if CMD == cmd:
				IP = re.search(pattern2,data).group()
				return IP

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Your argv is error')
	else:
		cmd = sys.argv[1]
		print(get_address(cmd))