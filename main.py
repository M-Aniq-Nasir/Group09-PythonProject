def M_Aniq_Nasir_calc():    
    while True:
        try:
            x=float(input("Enter First Number: " ))
            y=float(input("Enter Second Number: " ))
            
            
            print("Addition: "+str(x+y))
            print("Subtraction: "+str(x-y))
            print("Multiplication: "+str(x*y))
            if y != 0:
                print("Division",str(x/y))
            else:
                print("Second number cannot be zero.")
            
            break
        except:
            print("Please Enter numbers correctly.")
M_Aniq_Nasir_calc()