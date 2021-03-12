try: 
	num01 = input('请输入第一个数字')
	num02 = input('请输入第二个数字')
	result = num01 / num02
except BaseException as e:
	print('出错了',e)
else :
	print('计算结果为',result)