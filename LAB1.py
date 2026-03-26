
#question 1
name = input("What is your name? ")
print("Hello " + name + ".")
x= input("What is your Student ID? ")
print("Your ID is " + x )

#question 2

seconds=int(input("ENTER TOTAL SECONDS"))
hours= seconds//3600
mins= (seconds%3600)//60
remainseconds = seconds%60
print(seconds+ "is" + hours+ "," +mins + "and" +remainseconds)


#question 3
x1= float(input("ENTER x1 :"))
y1= float(input("ENTER y1:"))
x2= float(input("ENTER x2 :"))
y2= float(input("ENTER y2 :"))

a= x2- x1
b= y2-y1

distance= (a*a + b*b) ** 0.5


#question 4
print("*******/n*****/n***/n* ")