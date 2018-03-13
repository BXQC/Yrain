from sys import exit

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
index=['1st','2nd','3rd','4th','5th','6th']
L=len(animals)
for i in range(0,L):
	if i <= 2:
		print('The {} animal is at {} and is a {}'.format(index[i],i,animals[i]))
		exit(0)
	else:
		print('The {} th animal is at {} and is a {}'.format(i+1,i,animals[i])
#我不知道这样写有什么错误...此处留着,先试下只用for的循环嵌套,看可不可以...还是没找到问题所在....感觉break加在哪里都不对,run的时候提示的一直都是语法错误.....先留着,以后会了再回来DEBUG.....后面一篇中看到了exit(0)的用法,用于本篇去无济于事,总之是我还不太会用.先这样,等习惯了用法,再回来改.....
#'''for i in range(0,L):
#	print('The {} animal is at {} and is a {}'.format(index[i],i,animals[i]))'''
