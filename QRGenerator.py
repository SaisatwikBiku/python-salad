import qrcode 

str = input("Enter the URL: ")
myqr = qrcode.make(str)
myqr.save("myqr.png")