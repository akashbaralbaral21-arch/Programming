# question number:5

# from numpy import choose


# total_purchase_amount=int(input("Enter the total purchase amount:"))
# if total_purchase_amount>5000:
#     membership_status=input("do you have a membership card? (yes/no):")
#     if membership_status.lower()=="yes":
#         discount=(30/100)*total_purchase_amount
#         final_price=total_purchase_amount-discount
#         Total_saved=total_purchase_amount-final_price
#         print("you saved:", Total_saved)
#         print("The final price after discount is:",final_price)
#     else:
#         print("the final price without discount price is:", total_purchase_amount)
        
# else:
#     print("the final price without discount price is:", total_purchase_amount)
    
#question number:6
print("Welcome to the Magic Forest")
direction=input("Do you want to GO NORTH OR SOUTH?:")
if direction.lower()=="north":
    north=input("CROSS THE RIVER OR FOLLOW THE PATH?")
else:
    print("GAME OVER")
    
if north.lower()=="cross the river":
    print("GAME OVER")
else: 
    if north.lower()=="follow the path":
        choose=input("CHOOSE FAIR, OGRE OR ELF?")    
        if choose.lower()=="fairy":
            print("GAME OVER")
            print("END")
        elif choose.lower()=="ogre":
            print("GAME OVER")
        else:
            print("YOU WIN")
            print("GAME OVER")
    
    
    