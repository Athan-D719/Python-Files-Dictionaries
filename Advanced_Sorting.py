#SORTED()
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1 #adds keys and values to the dict.
            #d   #it would work the same way as a dict is a list of keys.
y = sorted(d.keys(), key=lambda k: d[k], reverse=True)#sorts depending on the key values[numeric], and reverse it 
#if theres no key or reverse it will automatically sort
#the object as alphabetic

for k in y:
    print("{} appears {} times".format(k, d[k]))
#######################################################################
#DEF FUNCTION AS KEY
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

def g(k, d):
    return d[k]

sorted_values = sorted(dictionary, key=lambda x: g(x,dictionary), reverse=True)
########################################################################
#######################################################################
#BREAKING TUPS: Tuples sorted biult in function, iterates each element...
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
#len(fruit_name) as the sorting key new propiety
for fruit in new_order:
    print(fruit)

###########################################################################
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
##########################################################################
##########################################################################
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))
#########################################################################
#########################################################################

def last_four(x):
    a = []
    a=int(str(x)[4:])
    return a


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]


sorted_ids = sorted(ids, key=lambda s: last_four(s)) #last_four(ids)
print(sorted_ids)
####################################################################
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
      
sorted_id = sorted(ids, key= lambda s: int(str(s).strip()[4:]))

######################################################################
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

top_three = sorted(medals, key=lambda s: medals[s], reverse=True)[:3]
##################################################################
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']

z_winners = sorted(winners, key=lambda s: s.strip()[0], reverse=True)
######################################################################
