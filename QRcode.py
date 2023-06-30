import qrcode
NameAndNum = input("pls enter your name and number")
QC = qrcode.make(NameAndNum)
QC.save("name and number QRcode.png")
