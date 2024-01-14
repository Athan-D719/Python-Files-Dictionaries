punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(x):
    n = ''
    for i in x:
        for j in i:
            #print(j)
            if j in punctuation_chars:
                x.replace(j, ' ')
                #print(x)
            else:
                n += j
    return(n)   


def get_pos(u):
    p = 0
    for i in u.split():#strip_punctuation(u.split()):
        if strip_punctuation(i.lower()) in positive_words:
            p += 1
    print('-------------------')
    return(p)   


def get_neg(u):
    p = 0
    for i in u.split():#strip_punctuation(u.split()):
        if strip_punctuation(i.lower()) in negative_words:
            p += 1
    return(p) 



# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

with open("project_twitter_data.csv","r") as r:
    f = r.readlines()
    n_rt =[]
    n_rp =[]
    n_po =[]
    n_ne =[]
    n_net =[]
    #with open("resulting_data.csv","w") as r:
    for row in f[1:]:
        val = row.strip().split(',')
        n_rt.append(val[1])
        n_rp.append(val[2])
        n_po.append(get_pos(val[0]))
        n_ne.append(get_neg(val[0]))
    for i in range(len(n_po)):
        n_net.append((int(n_po[i])-int(n_ne[i])))
        #print(n_rt,n_rp,n_po,n_ne,n_net)
        print(n_rt)
        print(n_rp)
        print(n_po)
        print(n_ne)
        print(n_net)
        #r.write("{},{},{},{},{}".format(n_rt,n_rp,n_po,n_ne,n_net))
        #r.write("\n")
        #return(n_rt,n_rp,n_po,n_ne,n_net)

with open("resulting_data.csv","w") as r:
    r.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    r.write("\n")
    for i in range(len(n_rt)):
        r.write("{},{},{},{},{}".format(n_rt[i], n_rp[i],n_po[i],n_ne[i],n_net[i]))
        r.write("\n")