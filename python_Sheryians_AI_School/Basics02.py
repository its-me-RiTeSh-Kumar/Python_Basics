"""a= int (input('Enter the first number '))
b=int (input('Enter the Second number '))
if (a>b):
    print ('A is greater then B')
elif(a==b):
    print ('A and  B are Equal')
else :
    print ('B is greater then A')"""
year = int (input('Enter the year :-'))
if year%400==0 or ( year%4==0 and year%100!=0 ):
    print ( "the Year is a leap year ")
else :
    print (" The Year is Not a leap year ")
