from faker import Faker 
from time import sleep
X = Faker()
while True:
	sleep(0.1)
	x = (X.user_name())
	print(x)
	with open('List.txt','a')as file:
		file.write(x+'\n')