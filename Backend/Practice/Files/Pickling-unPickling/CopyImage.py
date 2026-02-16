# scrfile=input("Entera file source :")
with open("C:\\Users\\kunal\\OneDrive\\Pictures\\Saved Pictures\\images.jpeg","rb") as rp:
    with open("possible.png","ab") as wp:
        imgdata=rp.read()
        wp.write(imgdata)
        print("File Copied---verify")




