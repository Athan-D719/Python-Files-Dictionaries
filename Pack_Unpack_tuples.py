#PACKING TUPLES:
def circleinfo(r):
    """Return (circunference,area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return(c,a)
print(circleinfo(10))
##########################################################
##########################################################
#UNPACKING TUPLES:
def add(x,y):
	return(x+y)
print(add(3,4))
z = (5,4)
print(add(*z)) #this line will cause the values to be unpacked
#print(add(z)) # this line will cause an error
###########################################################
#ITERATING UNPACKING:
d = {"k1:" 3, "k2:" 7,"k3:" "some other value"}

for p in d.items():
    print("key: {}, value: {}".format(p[0],p[1]))
    #item[0] = keys
    #item[1] = values
for k,v in d.items():
    print("key: {}, value: {}".format(k,v))
    #Exactly the same reultas.