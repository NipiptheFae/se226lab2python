x = input("Please choose a number between 3 and 9 \n")
for i in range(int(x)):
    if i == 0:
        print("*")
    elif i == 1:
        print("**")
    elif i == 2:
        print("***")
    elif i == 3:
        print("****")
    elif i == 4:
        print("*****")
    elif i == 5:
        print("******")
    elif i == 6:
        print("*******")
    elif i == 7:
        print("********")
    elif i == 8:
        print("*********")

j = 9-int(x)
for j in range(j+1,9):
    if j == 0:
        print("*********")
    elif j == 1:
        print("********")
    elif j == 2:
        print("*******")
    elif j == 3:
        print("******")
    elif j == 4:
        print("*****")
    elif j == 5:
        print("****")
    elif j == 6:
        print("***")
    elif j == 7:
        print("**")
    elif j == 8:
        print("*")



