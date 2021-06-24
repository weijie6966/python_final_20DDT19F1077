for x in range(1,6):
    print(f'You {x} time to try')
    password=input("Enter Password :")

    if(password=="abc123"):
        print("Login Successful!")
        break
    else:
        print("The password is incorrect, please re-enter")

    if(x==5):
        print("They were blocked by the system after five failed attempts")
