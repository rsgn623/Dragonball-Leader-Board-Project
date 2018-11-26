from appJar import gui
import numpy as np
import cv2
app = gui("Dragonball Fighterz Leaderd Board Creator")

app.addLabelEntry("Left Side Text")
app.addLabelEntry("Right Side Text")
app.getEntry("Left Side Text")
app.getEntry("Right Side Text")
    

#Choose number of players that will be present on leaderboard 
app.addOptionBox("Number of Players", ["4", "5", "6", "7", "8", "9", "10"])
for x in range(1, 5):
    app.addLabelEntry("Player %d" % x)
for y in range(1, (4*3)+1):
    app.addLabelOptionBox("Character %d" % y, ["Android 16", "Anroid 17", "Android 18", 
    "Android 21", "Bardock", "Beerus", "Broly", "Cell", "Cooler", "Frieza", "Ginyu", 
    "Gohan (Adult)", "Gohan (Teen)", "Goku (Base)", "Goku (SSJ)", "Goku (SSB)", "Goku Black",
    "Gotenks", "Hit", "Krillin", "Nappa", "Piccolo", "Tien", "Trunks", "Vegeta (Base)",
    "Vegeta (SSJ)", "Vegeta (SSB)", "Vegito", "Yamcha", "Zamasu" ])    

lastCount = 4  
def addPlayerEntries():
    global lastCount
    y = int(app.getOptionBox("Number of Players")) 
    if y == lastCount:
        pass       
    elif lastCount != y:
        for x in range(1, lastCount+1):
            app.removeEntry("Player %d" % x)
        for x in range(1, (lastCount*3)+1):
            app.removeOptionBox("Character %d" % x)
        for x in range(1, y+1):
            app.addLabelEntry("Player %d" % x)
            app.addCharacterChoices
        for x in range(1,(y * 3)+1):
            app.addLabelOptionBox("Character %d" % x, ["Android 16", "Anroid 17", "Android 18", 
        "Android 21", "Bardock", "Beerus", "Broly", "Cell", "Cooler", "Frieza", "Ginyu", 
        "Gohan (Adult)", "Gohan (Teen)", "Goku (Base)", "Goku (SSJ)", "Goku (SSB)", "Goku Black",
        "Gotenks", "Hit", "Krillin", "Nappa", "Piccolo", "Tien", "Trunks", "Vegeta (Base)",
        "Vegeta (SSJ)", "Vegeta (SSB)", "Vegito", "Yamcha", "Zamasu" ])
    lastCount = y
    print("%d" % lastCount)


app.setOptionBoxChangeFunction("Number of Players", addPlayerEntries)

#function overlays transparent image on background
def transparentOverlay(src , overlay , pos=(0,0),scale = 1):
    """
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image to be blit.
    :param scale : scale factor of transparent image.
    :return: Resultant Image
    """
    overlay = cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    h,w,_ = overlay.shape  # Size of pngImg
    rows,cols,_ = src.shape  # Size of background Image
    y,x = pos[0],pos[1]    # Position of PngImage
    
    #loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x+i >= rows or y+j >= cols:
                continue
            alpha = float(overlay[i][j][3]/255.0) # read the alpha channel 
            src[x+i][y+j] = alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]
    return src
def createImage():
    #read background 
    backgroundImg = cv2.imread('empty blue ice.png', cv2.IMREAD_COLOR)
    img21 = cv2.imread('char images/18.png', cv2.IMREAD_UNCHANGED)
    result = transparentOverlay(backgroundImg,img21,(300,0),0.7)
    
    cv2.imshow("image", result)  
    
app.addButton("Create Image", createImage)

app.go()

    

    
    