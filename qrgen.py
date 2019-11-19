#!/usr/bin/python3
import qrcode
import os
from PIL import Image


def Transparent(image_directory):
    img = Image.open(image_directory)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(image_directory, "PNG")


print("=====================QR CODE Generator=====================")
while True:
    user_input = input("Do you want to create QR Code (Y/N): ")
    if user_input == "Y":
        text = input("Info in QR Code: ")
        store = input(
            "Enter file name (example: qrcode.png) or write path to future file: ")
        if store == '':
            store = "qrcode.png"
        img = qrcode.make(text)
        img.save(store)
        if os.path.isfile(store):
            print(f"Your QR code ({store}) succesfully created!)")
        else:
            print("Something gone wrong, try again")
            continue
        user_transparent = input(
            "Do you want to make your QR code transparent? (Y to confirm): ")
        if user_transparent == "Y":
            Transparent(store)
        else:
            print("No transparecy, ok!")

        user_open = input(
            "Do you want to open your newly created QR code? (Y to confirm): ")
        if user_open == "Y":
            qrimg = Image.open(store)
            qrimg.show()
        else:
            print("Do not open, got it!")
            continue
    elif user_input == "N":
        break
    else:
        print("Wrong input, try again")
        continue
        """
        TODO
        1.Add transparecy option (DONE)
        2.More intuitive interface (DONE)
        3.EXE
        4.GUI???
        """
