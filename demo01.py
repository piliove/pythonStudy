for item in range(3):
	pwd = input('请输入您的密码')
	if pwd == '8888' :
		print('输入密码正确')
		break
	else :
		print('输入密码不正确')
else :
	print('您输入的三次密码不正确')