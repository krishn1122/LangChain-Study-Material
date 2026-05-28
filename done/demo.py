from typing import Union
ID: Union[str, int] = input("Enter your college ID: ")
x = ID.upper()

if x == "20AI016":
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
        n = int(input("Enter your option: "))
        
        if n == 1:
            print("""               -- Account Information --
                                    Name: Krishn Jatav
                                    Age : 21
                                    ID  : 20AI016 
                                    
                                    Enter 0 to Exit!""")
        
        elif n == 2:
            print(''' ! Service Under Maintenance.
                        
                                    Enter 0 to Exit!''')
        
        elif n == 3:
            print("""* Error: No game Found! *
                            
                                    Enter 0 to Exit!""")
        
        elif n == 0:
            print("Exiting...")
            break
        
        else:
            print("Invalid option, please try again.")

else:
    print("** Error: Invalid ID **")
