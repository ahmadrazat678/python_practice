import qrcode


url = input("Enter text or url : ")
img = qrcode .make(url)
img.save("qrcode.png")
print("qrcode created successfully")