##############################################
#ACTUAL WAY
fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4
###################################################
##############################################
#READING THE ENTTIRE FILE
f = open("file_name.txt","r") #Read only
#f = open("file_name.txt","w") #write
entire_file = f.read()#[:40]
print(entire_file)

f.close()
################################################
#READING FILE SPECIFIED LINES
f = open("file_name.txt","r") 

l = f.readline() #First Line
print(l)
print("This is a new line: \n")
# \n for 'Enter'
l = f.readline()
print(l)

f.close()
###############################################
#READ LINES AS A LIST:
f = open("file_name.txt","r") 

lines_list = f.readlines() 
#This method saves every line as an element from a list
#print(lines_list[:4])
for line in lines_list:
    #Iterating through the list.
    print("line read: " + line)
    #as the print method returns the '\n' as well
    #we can suppress that space getting rid of the
    #white spaces..
    print(lines.strip())

    #OR itterate trough the file itselff:
  ..lines in f:...  

f.close()
##############################################
#using the 'with code block
#All the file processing inside the 'with' code block
#Exiting the with would automatically close the file.
with open("file_name", "r") as f:
    lines_list = f.readlines()
    for line in lines_list:
        print("line read: " + line) 
######################################################
######################################################
#USING THE METHOD SPLIT()...EVERY ','
olypmicsfile = open("olypmics.txt", "r")

#for aline in olypmicsfile.readlines():
for aline in olypmicsfile: #simpler way to iterate trough the lines
    values = aline.split(",") #every ',' it splits it and appends it
                              #into the list object
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()
######################################################
#FINDING PATHS IN THE SYSTEM
######################################################
#THERES AN ABSOLUTE PATH OR THE PATH WE GIVE FROM SOMEWHER:
#Absolute ; /Users/Asus/OneDrive/Python(FIles-Dictionaries)
#Relative ; .../Python(FIles-Dictionaries)
