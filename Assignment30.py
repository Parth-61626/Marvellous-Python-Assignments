import sys

# 1)

file_name = sys.argv[1]

obj1 = open(file_name,"r")
rl = obj1.readlines()
print("Number of lines in file :",len(rl))
obj1.close()


# 2)
def Countword(fname):
    fobj=open(fname,"r")
    count=0

    for line in fobj:
        words=line.split()
        count+=len(words)


        fobj.close()
        return  count
    
def main():
    filename=sys.argv[1]
    Ret=Countword(filename)
    print("Total number of word in",filename,";",Ret)


if __name__ == "__main__":
    main()      

# 3)
def DisplayContent(fname):
    fobj=open(fname,"r")

    for line in fobj:
        print(line,end="")
    fobj.close()
def main():
    fname=sys.argv[1]
    DisplayContent(fname)
if __name__ == "__main__":
    main() 

# 4)
def Copyfile(first,second):
    f1first=open(first,"r")
    f2second=open(second,"w")

    for line in f1first:
        f2second.write(line) 

    f1first.close()
    f2second.close()

def main():
    fst=sys.argv[1]
    sec=sys.argv[2]
    Copyfile(fst,sec)
    print("copied file succesfully")

        

if __name__ == "__main__":
    main()    

# 5)
def Searchwords(fname,word):
    fobj=open(fname,"r")
    data=fobj.read()
    fobj.close()

    if word in data :
        return True
    else:
        return False
def main():
    filename=sys.argv[1]
    word=sys.argv[2]
    Ret=Searchwords(filename,word)

    if Ret == True:
        print("Words",word,"is found in",filename )
    else:
         print("Words",word," not found in",filename )

if __name__ == "__main__":
    main() 