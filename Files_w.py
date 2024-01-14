#When writting onto a file if this one does not exist
#it will create it automatically
f = open("file_name.txt","w")
#if it does exist you would lose any data related to that file.
f.write("my last line\n")
f.write("my new last line\n")

f.close()
###################################################
###################################################
#ACTUAL WAY
with open("file_name.txt","w") as f   
    f.write("my last line\n")
    f.write("my new last line\n")
###################################################
###################################################
#EXCERCISE:
filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()
####################################################
