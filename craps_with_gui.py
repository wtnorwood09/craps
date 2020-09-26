from tkinter import *
import random



def crap_game():

	dice_1= input(""" Please enter 'roll' """)
	die_1=[1,2,3,4,5,6]
	die_2=[1,2,3,4,5,6]

		
	roll_1=random.choice(die_1)+ random.choice(die_2)
	
		
	if dice_1=='roll'and roll_1 == 7 or roll_1== 11:
		print(str(roll_1)+" You Win!")
		return
		
	elif dice_1=='roll' and roll_1 == 2 or roll_1 == 3 or roll_1 == 12:
		print(str(roll_1)+" You Lose")
		return

	else:
		print(str(roll_1))
		

	while True:
		roll_2=random.choice(die_1)+ random.choice(die_2)
		dice_2= input("""Type 'roll' again. """)
		if dice_2=='roll' and roll_2==7:
			print(str(roll_2)+" You Lose!")
			break
			return
			
		elif dice_2=='roll' and roll_2==roll_1:
			print(str(roll_2)+" You Win!")
			break
			return
		elif dice_2=='roll' and roll_2 !=7 or roll_2 != roll_1:
			print(str(roll_2)+" Roll Again! Come on Big Money! ")


			


root = Tk(className = 'game - Craps')

root.geometry("500x200")

label_1=Label(root, text="Welcome to Craps", bg="Red")
label_1.pack(side=TOP, fill=X)

roll_button = Button(root, text='Roll!', height=2, width=20, command=crap_game)
roll_button.pack(side=BOTTOM, padx=20, pady=5)



root.mainloop()