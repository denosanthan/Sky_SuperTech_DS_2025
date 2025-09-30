master_pin= "0123"
pin= None
attempts=0

while pin != master_pin and attempts < 3:
    pin = input("Enter the pin: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # ONLY EXECUTE ONCE if while loop becomes False!

    print("Done")