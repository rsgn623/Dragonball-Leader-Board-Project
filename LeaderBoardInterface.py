from appJar import gui
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image  

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
    #imagedraw using custom font
    cv2_im_rgb = cv2.cvtColor(backgroundImg,cv2.COLOR_BGR2RGB) 
    pil_im = Image.fromarray(cv2_im_rgb)  
    draw = ImageDraw.Draw(pil_im)  
    font = ImageFont.truetype("Arial.ttf", 25)
    fontSmaller = ImageFont.truetype("Arial.ttf", 20)
    fontSmallest = ImageFont.truetype("Arial.ttf", 15)
    playerNumber = int(app.getOptionBox("Number of Players"))
    #if statements to write names for number of players
    if playerNumber == 4:
        for x in range(1, 4):
            nameCoord = (82 + ((-1+x)*600),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
        for x in range(4, 5):
            nameCoord = (682,451) 
            draw.text(nameCoord, "%d " % x + app.getEntry("Player %d" % x), font=font, fill="black")
    if playerNumber == 5:
        for x in range(1, 4):
            nameCoord = (82 + ((-1+x)*600),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
        for x in range(4, 6):
            nameCoord = (82 + ((-4+x)*600),451) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
    if playerNumber == 6:
        for x in range(1, 4):
            nameCoord = (82 + ((-1+x)*600),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
        for x in range(4, 7):
            nameCoord = (82 + ((-4+x)*600),451) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
    if playerNumber == 7:
        for x in range(1, 4):
            nameCoord = (82 + ((-1+x)*600),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmaller, fill="black")
        for x in range(4, 7):
            nameCoord = (82 + ((-4+x)*600),451) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmaller, fill="black")
        for x in range(7, 8):
            nameCoord = (682,661) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmaller, fill="black")
    if playerNumber == 8:    
        for x in range(1, 5):
            nameCoord = (82 + ((-1+x)*400),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmallest, fill="black")
        for x in range(5, 9):
            nameCoord = (82 + ((-5+x)*400),501) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmallest, fill="black")
    if playerNumber == 9:    
        for x in range(1, 6):
            nameCoord = (82 + ((-1+x)*300),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmallest, fill="black")
        for x in range(6, 10):
            nameCoord = (82 + ((-6+x)*300),501) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmallest, fill="black")  
    if playerNumber == 10:    
        for x in range(1, 6):
            nameCoord = (82 + ((-1+x)*300),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmallest, fill="black")
        for x in range(6, 11):
            nameCoord = (82 + ((-6+x)*300),501) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmallest, fill="black")          
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR) 
    #test image resize 
    smaller18 = cv2.resize(img21, (0,0), fx=0.5, fy=0.5) 
    #if statement to place characters on leaderboard

    def getCharImageFromEntry:
        playerNumber = int(app.getOptionBox("Number of Players"))
        for x in range(1, )



    result = transparentOverlay(cv2_im_processed,smaller18,(300,0),0.7)

    """
    def getPlayerValues():
        playerValues = {}
        for x in range(1,4):
            #makes list of player name and characters they play
            playerValues["Player %d Name" % x] = app.getEntry("Player %d" % x)
            playerValues["Character %d" % x] = app.getOptionBox("Character %d" %x)
            playerValues["Character %d" % (x + 1)] = app.getOptionBox("Character %d" % (x + 1))
            playerValues["Character %d" % (x + 2)] = app.getOptionBox("Character %d" % (x + 2)) 
    app.getPlayerValues()
    """
    cv2.imshow("image", result)  
    

    
    
app.addButton("Create Image", createImage)

app.go()

    

    
    