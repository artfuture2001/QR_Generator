#!/usr/bin/python3
import qrcode

while True:
    user_input = input("Create qrcode? ")
    if user_input == "Y":
        text = input("What will be in qr code? ")
        store = input("Name file or add path to file? ")
        if store == " ":
            store = "qrcode.png"
        img = qrcode.make(text)
        img.save(store)

    elif user_input == "N":
        break
    else:
        print("Wrong input, try again")
        continue
        """
        TODO
        1.Add transparecy option
        2.More intuitive interface
        3.GUI???
        """
