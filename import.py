import random

print('\n這是一個猜數字的遊戲\n')
min = input('請輸入最低範圍（含）')
min = int(min)
max = input('請輸入最高範圍(含）')
max = int(max)
r = random.randint(min,max)
i = 0
while True:
	i = i + 1
	user = input('\n請輸入你猜的數字：')
	if int(user) > r:
		print('\n太大了')
	elif int(user) < r:
		print('\n太小了')
	else:
		print('\n你猜對了嘿嘿嘿！')
		print('\n你一共猜了',i,'次哦！')
		break