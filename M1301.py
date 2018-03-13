hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']
elements=[]
for number in the_count:
	print('this is cout {}'.format(number))

for fruit in fruits:
	print('a fruit of type:%s'%fruit)

for i in change:
	print('i got %r'%i)

for i in range(0,6):
	print('adding %d to the list.'%i)
	elements.append(i)

for i in elements:
	print('element was : %d'%i)

