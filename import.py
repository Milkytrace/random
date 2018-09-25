import random

print('\n這是一個猜數字的遊戲\n')
r = random.randint(1,100)
while True:
	user = input('\n請輸入你猜的數字（在1-100之間，包括）：')
	if int(user) > r:
		print('\n太大了')
	elif int(user) < r:
		print('\n太小了')
	else:
		print('\n你猜對了！')
		break