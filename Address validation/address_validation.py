user = input("Please enter your address: ")
if((user.find("@") == -1 or user.find(".") == -1) ):
    print("invalid address")
else :
    print("valid address")
