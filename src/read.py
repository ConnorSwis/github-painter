from PIL import Image


img = Image.open('./src/design.bmp')

colors = {
    (27, 31 , 35) : 0,
    (14, 68 , 41) : 1,
    (0 , 109, 50) : 2,
    (38, 166, 65) : 3,
    (57, 211, 83) : 4
}

data = img.getdata()

cList = []

for i in ROWS:
    #put in every {column number}'th value. im too high for this. you know how to do that
    #keep in mind that the calandar moves to the right overall as time moves on. IE you might have to flip the list. picture a printer
    bList=["see comment"]
    cList.append(bList)