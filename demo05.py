try: 
	num01 = input('�������һ������')
	num02 = input('������ڶ�������')
	result = num01 / num02
except BaseException as e:
	print('������',e)
else :
	print('������Ϊ',result)