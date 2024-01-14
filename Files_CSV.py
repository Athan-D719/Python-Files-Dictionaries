#CSV: Coma Separated Values
#Automatically try to open it as a spreadsheet(Excel)
#:Name,hehe,jojo   # columns(down the files..)
# jiojio,sjasj,dskl # if theres no coma before means new columns
########################################################
#a = '''Name,score,grade
#Jamal,98,A+
#Eloise,87,B+
#Madeline,99,A+
#Wei,94,A'''
#with open("grades.csv","w") as f:
#    f.write(a)
########################################################
#CSV FORMAT READING
 with open('olympics.txt', 'r') as fileconnection
 lines = fileconnection.readlines()
 header = lines[0]
 field_names = header.strip().split(',')
 print(field_names)
 for row in lines[1:]:
     vals = row.strip().split(',') #strip() to get rid of the \n
     #.split('|') or .split('\\t') other ways
     if vals[5] != "NA":
         print("{}: {}; {}".format(
                 vals[0],
                 vals[4],
                 vals[5]))
'''"Name","Sex","Age","Team","Event","Medal"
"A Dijiang","M","24","China","Basketball","NA"
"Edgar Lindenau Aabye","M","34","Denmark/Sweden","Tug-Of-War","Gold"
"Christine Jacoba Aaftink","F","21","Netherlands","Speed Skating, 1500M","NA"'''
##########################################################
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    #row_string = ','.join([olympian[0], str(olympian[1], olympian[2])])
    #row_string = ','.join(olympian)
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    #row_line = olympian[0] + ',' olympian[1] + ',' olympian[2]
    outfile.write('\n')
outfile.close()
##########################################################################
#####################################################################
with open('SP500.txt', 'r') as f:
    lines = f.readlines()
    header = lines[0]
    field_names = header.strip().split(',')
    #print(field_names)
    SP = list()
    interest = list()
    mean_SP = float()
    max_interest = float()
    for row in lines[6:18]:
        vals = row.strip().split(',')
        #print(vals[0])
        SP.append(float(vals[2]))
        interest.append(float(vals[5]))
    mean_SP = sum(SP)/len(SP)
    print(mean_SP)
    max_interest = max(interest)
    print(max_interest)
    
