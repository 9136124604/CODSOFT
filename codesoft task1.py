#task1 simple calculator 
#all the operations present in the simple calculator 
#1.addition
#2.subtraction
#3.multiplication
#4.division
print("simple calcultor")
a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division \npress 5 for exiting the calculator")
#we have to give user a choice therefore create a choice variable
while True:
#we'll print everything in a while loop so that the program executes infinitely until we till it to stop
 choice=int(input("enter your choice from 1-5: "))
#now use conditional statements 
 if choice==1:
     print(a+b)
 elif choice==2:
     print(a-b)
 elif choice==3:
     print(a*b)
 elif choice==4:
     print(a/b)
 elif choice==5:
     print("exiting the calculator")
     break
 else:
     print("invalid choice")
