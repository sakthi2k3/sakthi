sw=[]
with open("stopwords.txt", "r") as f:
            lines = f.readlines()
for line in lines:
    if line!='\n':
         t=line.strip("\n")
         sw.append(t.strip())
print(sw)              
