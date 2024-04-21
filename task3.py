import random
num=int(input("Enter the Number :"))
gnum = random.randint(1, 9)
print("randam Number :",gnum)
if(num==gnum):
    print("Well Guessed")
else:
    print("Incorrect guess. Try again.")

