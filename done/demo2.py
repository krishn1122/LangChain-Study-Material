from typing import Union
ID:Union[str,int]=input("Enter your ID: ")
id="20AI016"
x=ID.upper()
if x==id:
    print(" ")
    print("                         ** Login Successfully **                       ")
    print(" ")
    print("                         Welcome Krishn Jatav!                         ")
    print("""             -- Choose the following Options --
                                1. Account Info
                                2. Update Account
                                3. Game mode
                
                                                                                """)
    
    while True:
        n=int(input("Enter your response: "))
        if n==1:
            print("No Account found!")

            print(" Enter 0 for Exit!")
        elif n==2:
             print("No Account found!")

             print(" Enter 0 for Exit!")
        elif n==0:
            print("Exiting...")
            break
else:
    print(" Invalide ID.")