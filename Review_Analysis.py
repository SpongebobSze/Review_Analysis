#Review Analysis
#task1:print out the average length of each review
#task2:print out the number of the reviews that include 'good'(2 styles for appending)
#task3:print out the numbe of the reviews whose length is less than 100

# task1:
BOX = []
box = 0
with open('053 reviews.txt' , 'r') as file:
	for line in file:
		BOX.append(line) #不一定非得要加line，可以是数字、字串、布林值、运算公式
		box += len(line)
print('The average length of the reviews is' , box / len(BOX))
print('------------------------------------------')
# task2:
with open('053 reviews.txt' , 'r') as file:
	BOX2 = [1 for line in file if 'good' in line] #advanced 
print('The number of this type of reviews is', len(BOX2))	
print('style2-------------------------------------')
BOX3 = []
with open('053 reviews.txt' , 'r') as file:
	for line in file:
		if 'good' in line:
			BOX3.append(1)
print('The number of this type of reviews is', len(BOX3)) 
print('------------------------------------------')
# task3:
with open('053 reviews.txt' , 'r') as file:
	BOX4 = [1 for line in file if len(line) < 100]
print('The number of this type of reviews is', len(BOX4))


