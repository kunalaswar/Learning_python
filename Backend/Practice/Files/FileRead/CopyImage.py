  #!program for copying the Image (Binary file --denoated by a letter b)
  #CopyImage.py
def CopyImage():
    try:    
        with open("C:\\Users\\kunal\\OneDrive\\Pictures\\Saved Pictures\\nothing.jpeg","rb") as rp:  
            with open("CopyImage.png","wb") as wp:
                Imgdata=rp.read()
                wp.write(Imgdata)

            print("File Image is copy Succesfully")    
            
    except FileNotFoundError:
        print("File is Not found to copy ")

CopyImage()
