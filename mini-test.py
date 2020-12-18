######################################
# Usage
#
# Input: [2,3]
# Output: ad ae af bd be bf cd ce cf
#
# Input: [9]
# Output: w x y z
#
######################################

import re

mapping_list = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
start_flag=False  # avoid redundant space

def recur_print(input_num, depth, output, n):
	if(depth == n):
		global start_flag
		if start_flag:
			print(' ', end='')
		else:
			print('Output: ', end='')
		start_flag = True
		print(''.join(output), end='')
		return


	for i in range(len(mapping_list[input_num[depth]])):
		output.append(mapping_list[input_num[depth]][i])
		recur_print(input_num, depth + 1, output, n)
		output.pop()
		if(input_num[depth] == 0 or input_num[depth] == 1):
			return

if __name__ == '__main__':
	input_str = input('Input: ')
	if re.fullmatch('^\[\s*[2-9]{1}(\s*,\s*[2-9]{1})*\s*\]$', input_str):
		input_num = list(map(int, re.findall("[2-9]{1}",input_str)))
		n = len(input_num)
		# if n>10:
		# 	print ('are you sure to calcu? ')
		# 	return
		recur_print(input_num, 0, [], n)

	else:
		print('Check your input! (example: [2,3] or [9])')

