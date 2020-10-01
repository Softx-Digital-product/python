
for i in range(1):
    text = input("Enter Text Here : ")
    f = open("data.txt","a")
    f.write(" " +text +"\n ")
    f =open("data.txt", "r")
    print(f.read())

    f.close()

#for i in range(10):
    f = open("data.txt","r")
    print(f.readline())
