# To comment anything use hastag '#'
"""doc String use to write mutilple comment but not basically not its proper is multiple comments Lines"""
print("Hi Python")
#"""AnmolRatan --> pascal case """
# anmolRatan --> camel case 
# anmol_.ratan --> snake case 
a=5 
b=2.3
c=2/4
d= 24j
#print (type(a)) -o/p-> <class 'int'>
#print (type(b))-o/p-><class 'float'>
#print (type(c))-o/p-><class 'float'>
#print (type(d))-o/p-> <class 'complex'>
string="anmolratan"

#print (type(string))-o/p-><class 'str'>
## String +ve & -ve indexing 
print ( string[4])

print ( string[4],string[-7])
#print ( string[18]) --> IndexError: string index out of range
#String  Slicing
a1="Anmol Ratan"
print(a1[0:5:1])
print(a1[6::1])
#Type Convsersion 
e=1234
e=str(e)
print (type(e))
# input String
sc=input (" Enter the Output")
print (sc)
age =int(input ('Enter the Age'))
print (age)