# --- Guess Number Game ---

import random
print("****\tGuess Number Game\t****")
num=random.randint(1,100)
count=5
find=False
print("\n\tYou Have only 5 attempt to Win..")
while count>=1:
	user=int(input("Enter Your number(1-100): "))
	if 0<user<100:
		if user<num:
			print("\t Your number is smaller")
			count-=1
			print("You have only ",count, "attempt left")
			continue
		elif user>num:
			print("\t Your number is greater")
			count-=1
			print("You have only ",count, "attempt left")
			continue
		elif user==num:
			print("\n*$*\tYou Got it\t*$*")
			find=True
			break
	else:
		print(":(  Wrong Input! ")

if find==False:
	print("\t:( YOU FAILED :(")
	print("The Secret Number is ",num)
else:
	print(" :) Congrants")
	