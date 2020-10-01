




def rent_data():

    print("="*30)
    date= input("Enter Date of Rent  amount is paying: (dd/mm/yyyy) : ")

    amt = int(input("Enter Rent Amount paying : "))

    electricity= int(input("Enter Electricity Bill Amount : "))
    elediv= electricity/2
    print("Electricity Bill Divided  : ",elediv)

    water= int(input("Enter Water Bill Amount :"))
    watdiv= water/2
    print("water Bill Divided  : ",watdiv)

    Tax = int(input("Enter Tax Bill Amount :"))
    taxdiv= Tax/2
    print("Tax Bill Divided  : ",taxdiv)
    print("="*70)

    total= amt+elediv+watdiv+taxdiv
    inttotal = int(total)
    stringtotal= str(inttotal)
    print("Total Amount of ",date," is ",stringtotal)

    choose = int(input("Enter 1 to save Rental Details : "))

    if choose ==1:

        file= open("Rental.txt",'a')
        file.write("\n \n")
        #file.write("================================== Rental payment Details ===========================")
        #file.write('\n \n')
        file.write("Date of Rental Amount paid :> ")
        file.write(date)
        file.write("\t \t")
        file.write("Rental Amount paid :> ")
        file.write(stringtotal)
        file.close()

        print("****** Rental payment Details Saved ****** ")

    else:
        print("Thanks for using ")




def rental_ds():
    print("="*30)
    rfn= input("Enter Rental First Name : ")
    rmn = input("Enter Rental Middle Name : ")
    rln = input("Enter Rental Last Name : ")

    rem= input("Enter Rental Email Id : ")
    rph= input("Enter  Rental Phone No : +91 ")

    rdp= input("Enter Rental Deposit Amount : ")
    rdt= input("Enter Deposit Given Date :(dd/mm/yyyy) : ")
    rrp= input("Enter per Month Rent Amount : ")

    rfm= input("Enter Rental No. of Member in Family : ")
    print("="*50)
    
    cs= int(input("Enter 1 to Save Details :> "))

    if cs == 1:
        file= open('Rental.txt','a')
        files.write("\n")
        files.write("===========================Rental Details =======================")
        files.write("\n")
        files.write("Rental full Name :> ")
        files.write(rfn)
        files.write(" ")
        files.write(rmn)
        files.write(" " )
        files.write(rln)
        files.write("\n")
        files.write("Rental Email Id :> ")
        files.write(rem)
        files.write("\t")
        files.write("Rental Phone No :>+91")
        files.write(rph)
        files.write("\n")
        files.write("Date of Deposite Paid :> ")
        files.write(rdt)
        files.write(" \t ")
        files.write("Rental Deposit Amount :> ")
        files.write(rdp)
        files.write(" \n")
        files.write("Rent Amount for per month :> ")
        files.write(rrp)
        files.close()
        print("="*50)
        print("Saved Rental  Details Successfully :) ")
    
    
    else :
        print("Thanks for using ")
        exitdata = input("press Y for Exit OR press N for Stay")

        if exitdata==('y'|'Y'):
            print("Exiting tata bye")
            exit()
        else :
            print("staying")


    
    



def owner_ds ():
    print("="*30)
    ofn= input("Enter Owner First Name : ")
    omn = input("Enter Owner Middle Name : ")
    oln = input("Enter Owner Last Name : ")

    oem= input("Enter Owner Email Id : ")
    oph= input("Enter  Owner Phone No : +91 ")

    ocity= input("Enter owner City Name : ")
    oad= input("Enter owner Address : ")
    opin= input("Enter owner pin code : ")

    cs= int(input("Enter 1 to Save Details :> "))

    if cs == 1:
        
        file = open('Rental.txt','w')
        file.write("===========================OWNER Details =======================")
        file.write("\n")
        file.write("Owner full Name :> ")
        file.write(ofn)
        file.write(" ")
        file.write(omn)
        file.write(" " )
        file.write(oln)
        file.write("\n")
        file.write("Owner Email Id :> ")
        file.write(oem)
        file.write("\t")
        file.write("Owner Phone No :>+91")
        file.write(oph)
        file.write("\n")
        file.write("Owner Address :> ")
        file.write(oad)
        file.write("\n")
        file.write("Owner City & PinCode :> ")
        file.write(ocity)
        file.write(" ")
        file.write(opin)
        file.close()
        print("Saved owner Details Successfully :) ")
    
    
    else :
        print("Thanks for using ")
        exitdata = input("press Y for Exit OR press N for Stay")

        if exitdata==('y'|'Y'):
            print("Exiting tata bye")
            exit()
        else :
            print("staying")

    

def main_body ():
    print(" [1] Add Owner Details ")
    print(" [2] Add Rental Details ")
    print(" [3] Rental Payment Details ")
    print(" [4] Sent Notificiation ")
    print(" [5] Exit")

    choose = int(input("Choose The service from above list :> "))

    if choose ==1:
        owner_ds()
        
    elif choose ==2:
        rental_ds()

    elif choose ==3:
        rent_data()

    elif choose ==4:
        print("choose 4")

    elif choose ==5:
        exit()
    else :
        print("please choose the correct service :(")
        main_body()
    print("Thanks for using")

if __name__ == "__main__":
    main_body()
