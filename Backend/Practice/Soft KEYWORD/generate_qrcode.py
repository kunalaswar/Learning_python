# import qrcode
# #generating a QR code using the make() function
# qr_img = qrcode.make("Welcome to the kunal QR code.")
# #saving the image file wih the Extension .jpg
# qr_img.save("QRcodeimg.jpg")
# print("QR code Generated")


import qrcode  
# generating a QR code using the make() function  
qr_img = qrcode.make("Read and write Python Notes to get the Job")      
# saving the image file  
qr_img.save("student.jpg")  
print("QR Code generated--verify")

