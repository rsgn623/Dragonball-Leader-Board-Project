from appJar import gui
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image  

app = gui("Dragonball Fighterz Leader Board Creator")

app.addLabelEntry("Left Side Text")
app.addLabelOptionBox("Left Side Text Color", ["Black", "Blue", "Grey", "Orange", "Red", "White", "Yellow"])
app.setOptionBox("Left Side Text Color", 6)
app.addLabelEntry("Right Side Text")
app.addLabelOptionBox("Right Side Text Color", ["Black", "Blue", "Grey", "Orange", "Red", "White", "Yellow"])
app.setOptionBox("Right Side Text Color", 4)


    

#Choose number of players that will be present on leaderboard 
app.addOptionBox("Number of Players", ["4", "5", "6", "7", "8", "9", "10"])
app.addLabelOptionBox("Color of Player Text", ["Black", "Blue", "Grey", "Orange", "Red", "White", "Yellow"])
app.setOptionBox("Color of Player Text", 0)
for x in range(1, 5):
    app.addLabelEntry("Player %d" % x)
for y in range(1, (4*3)+1):
    app.addLabelOptionBox("Character %d" % y, ["Android 16", "Android 17", "Android 18", 
    "Android 21", "Bardock", "Beerus", "Broly", "Cell", "Cooler", "Frieza", "Ginyu", 
    "Gohan (Adult)", "Gohan (Teen)", "Goku (Base)", "Goku (SSJ)", "Goku (SSB)", "Goku Black",
    "Gotenks", "Hit", "Kid Buu", "Krillin", "Majin Buu", "Nappa", "Piccolo", "Tien", "Trunks", "Vegeta (Base)",
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
        for x in range(1,(y * 3)+1):
            app.addLabelOptionBox("Character %d" % x, ["Android 16", "Android 17", "Android 18", 
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
global result
def createImage():
    #first, check user input
    if checkUserInput():
        pass
    else:
        return
    #read background image
    backgroundImg = cv2.imread('/Users/Stephen/Documents/Visual Studio Code Workspace/background/background.png', cv2.IMREAD_COLOR)
    #imagedraw using custom font
    cv2_im_rgb = cv2.cvtColor(backgroundImg,cv2.COLOR_BGR2RGB) 
    pil_im = Image.fromarray(cv2_im_rgb)  
    draw = ImageDraw.Draw(pil_im)  
    font = ImageFont.truetype("fonts/Arial.ttf", 25)
    fontSmaller = ImageFont.truetype("/Users/Stephen/Documents/Visual Studio Code Workspace/fonts/Arial.ttf", 20)
    fontSmallest = ImageFont.truetype("/Users/Stephen/Documents/Visual Studio Code Workspace/fonts/Arial.ttf", 15)
    dragonFont = ImageFont.truetype("/Users/Stephen/Documents/Visual Studio Code Workspace/fonts/saiyan.ttf", 150)
    #draws the left and right side text from the entry boxes. the saiyan fonts are only used for the header
    dragonFontLeft = ImageFont.truetype("/Users/Stephen/Documents/Visual Studio Code Workspace/fonts/saiyanleft.ttf", 60)
    dragonFontRight = ImageFont.truetype("/Users/Stephen/Documents/Visual Studio Code Workspace/fonts/saiyanright.ttf", 60)
    playerNumber = int(app.getOptionBox("Number of Players"))
    
    
    textColorLeft = str(app.getOptionBox("Left Side Text Color"))
    if textColorLeft is "Yellow":
        textColorLeft = (255,234,0)
    else:
        pass
    textColorRight = str(app.getOptionBox("Right Side Text Color"))
    if textColorLeft is "Yellow":
        textColorLeft = (255,234,0)
    else:
        pass
    textColorPlayer = str(app.getOptionBox("Color of Player Text"))
    if textColorPlayer is "Yellow":
        textColorLeft = (255,234,0)
    else:
        pass
    draw.text((30,10), app.getEntry("Left Side Text"), font=dragonFontLeft, fill=textColorLeft)
    draw.text((1000,10), app.getEntry("Right Side Text"), font=dragonFontRight, fill=textColorRight)
    draw.text((825,10), "O", font=dragonFont, fill="orange")
    #if statements to write names for number of players
    if playerNumber == 4:
        for x in range(1, 4):
            nameCoord = (82 + ((-1+x)*550),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
        for x in range(4, 5):
            nameCoord = (632,531) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
    if playerNumber == 5:
        for x in range(1, 4):
            nameCoord = (82 + ((-1+x)*550),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
        for x in range(4, 6):
            nameCoord = (82 + ((-4+x)*550),531) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
    if playerNumber == 6:
        for x in range(1, 4):
            nameCoord = (82 + ((-1+x)*550),171) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
        for x in range(4, 7):
            nameCoord = (82 + ((-4+x)*550),531) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=font, fill="black")
    if playerNumber == 7:
        for x in range(1, 4):
            nameCoord = (82 + ((-1+x)*550),141) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmaller, fill="black")
        for x in range(4, 7):
            nameCoord = (82 + ((-4+x)*550),401) 
            draw.text(nameCoord, "%d. " % x + app.getEntry("Player %d" % x), font=fontSmaller, fill="black")
        for x in range(7, 8):
            nameCoord = (632,631) 
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
    def getCharacterFromEntry(characterEntry):
        if(characterEntry == "Android 16"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/16.png"
        if(characterEntry == "Android 17"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/17.png"
        if(characterEntry == "Android 18"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/18.png"
        if(characterEntry == "Android 21"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/21.png" 
        if(characterEntry == "Bardock"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/bardock.png"  
        if(characterEntry == "Beerus"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/beerus.png"  
        if(characterEntry == "Broly"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/broly.png" 
        if(characterEntry == "Cell"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/cell.png" 
        if(characterEntry == "Cooler"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/cooler.png" 
        if(characterEntry == "Frieza"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/frieza.png" 
        if(characterEntry == "Ginyu"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/ginyu.png" 
        if(characterEntry == "Gohan (Adult)"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/gohanadult.png" 
        if(characterEntry == "Gohan (Teen)"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/gohanteen.png" 
        if(characterEntry == "Goku (Base)"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/gokubase.png" 
        if(characterEntry == "Goku (SSJ)"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/gokus.png" 
        if(characterEntry == "Goku (SSB)"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/gokublue.png" 
        if(characterEntry == "Goku Black"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/gokublack.png" 
        if(characterEntry == "Gotenks"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/gotenks.png" 
        if(characterEntry == "Hit"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/hit.png" 
        if(characterEntry == "Kid Buu"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/kbuu.png" 
        if(characterEntry == "Krillin"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/krillin.png" 
        if(characterEntry == "Majin Buu"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/mbuu.png" 
        if(characterEntry == "Nappa"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/nappa.png" 
        if(characterEntry == "Piccolo"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/piccolo.png" 
        if(characterEntry == "Tien"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/tien.png" 
        if(characterEntry == "Trunks"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/trunks.png" 
        if(characterEntry == "Vegeta (Base)"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/vegetabase.png" 
        if(characterEntry == "Vegeta (SSJ)"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/vegetas.png" 
        if(characterEntry == "Vegeta (SSB)"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/vegetablue.png" 
        if(characterEntry == "Vegito"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/vegito.png" 
        if(characterEntry == "Yamcha"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/yamcha.png" 
        if(characterEntry == "Zamasu"):
            return "/Users/Stephen/Documents/Visual Studio Code Workspace/char images/zamasu.png" 
#if statement to place characters on leaderboard    
    if playerNumber == 4:
        for x in range(1, 4):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3)    
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-1+x) *150),230),0.7)
        for x in range(4, 7):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)                
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-4+x) * 150),230),0.7)
        for x in range(7, 10):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(1182 + ((-7+x) * 150),230),0.7)
        for x in range(10, 13):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-10+x) * 150),600),0.7)
    if playerNumber == 5:
        for x in range(1, 4):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3)    
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-1+x) *150),230),0.7)
        for x in range(4, 7):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)                
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-4+x) * 150),230),0.7)
        for x in range(7, 10):
            characterEntry = app.getOptionBox("Character %d" % x)
            getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(1182 + ((-7+x) * 150),230),0.7)
        for x in range(10, 13):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-10+x) * 150),600),0.7)
        for x in range(13, 16):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-13+x) * 150),600),0.7)
    if playerNumber == 6:
        for x in range(1, 4):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3)    
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-1+x) *150),230),0.7)
        for x in range(4, 7):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)                
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-4+x) * 150),230),0.7)
        for x in range(7, 10):
            characterEntry = app.getOptionBox("Character %d" % x)
            getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(1182 + ((-7+x) * 150),230),0.7)
        for x in range(10, 13):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-10+x) * 150),600),0.7)
        for x in range(13, 16):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-13+x) * 150),600),0.7)
        for x in range(16, 19):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.3, fy=0.3) 
            result = transparentOverlay(cv2_im_processed,charResize,(1182 + ((-16+x) * 150),600),0.7)
    if playerNumber == 7:
        for x in range(1, 4):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25)    
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-1+x) *150),180),0.7)
        for x in range(4, 7):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)                
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-4+x) * 150),180),0.7)
        for x in range(7, 10):
            characterEntry = app.getOptionBox("Character %d" % x)
            getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(1182 + ((-7+x) * 150),180),0.7)
        for x in range(10, 13):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-10+x) * 150),431),0.7)
        for x in range(13, 16):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-13+x) * 150),431),0.7)
        for x in range(16, 19):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(1182 + ((-16+x) * 150),431),0.7)
        for x in range(19, 22):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(632 + ((-19+x) * 150),660),0.7)
    if playerNumber == 8:
        for x in range(1, 4):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25)    
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-1+x) *100),180),0.7)
        for x in range(4, 7):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)                
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(482 + ((-4+x) * 100),180),0.7)
        for x in range(7, 10):
            characterEntry = app.getOptionBox("Character %d" % x)
            getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(882 + ((-7+x) * 100),180),0.7)
        for x in range(10, 13):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(1282 + ((-10+x) * 100),180),0.7)
        for x in range(13, 16):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-13+x) * 100),511),0.7)
        for x in range(16, 19):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(482 + ((-16+x) * 100),511),0.7)
        for x in range(19, 22):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(882 + ((-19+x) * 100),510),0.7)
        for x in range(22, 25):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.25, fy=0.25) 
            result = transparentOverlay(cv2_im_processed,charResize,(1282 + ((-22+x) * 100),510),0.7)
    if playerNumber == 9:
        imageScale = .21
        for x in range(1, 4):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale)    
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-1+x) *90),180),0.7)
        for x in range(4, 7):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)                
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(382 + ((-4+x) * 90),180),0.7)
        for x in range(7, 10):
            characterEntry = app.getOptionBox("Character %d" % x)
            getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(682 + ((-7+x) * 90),180),0.7)
        for x in range(10, 13):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(982 + ((-10+x) * 90),180),0.7)
        for x in range(13, 16):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(1282 + ((-13+x) * 90),180),0.7)
        for x in range(16, 19):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-16+x) * 90),511),0.7)
        for x in range(19, 22):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.2, fy=0.2) 
            result = transparentOverlay(cv2_im_processed,charResize,(382 + ((-19+x) * 90),510),0.7)
        for x in range(22, 25):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(682 + ((-22+x) * 90),510),0.7)
        for x in range(25, 28):
            characterEntry = app.getOptionBox("Character %d" % x) 
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED) 
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(982 + ((-25+x) * 90),510),0.7)
    if playerNumber == 10:
        imageScale = .21
        for x in range(1, 4):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale)    
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-1+x) *90),180),0.7)
        for x in range(4, 7):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry)                
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(382 + ((-4+x) * 90),180),0.7)
        for x in range(7, 10):
            characterEntry = app.getOptionBox("Character %d" % x)
            getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=imageScale, fy=imageScale) 
            result = transparentOverlay(cv2_im_processed,charResize,(682 + ((-7+x) * 90),180),0.7)
        for x in range(10, 13):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.2, fy=0.2) 
            result = transparentOverlay(cv2_im_processed,charResize,(982 + ((-10+x) * 90),180),0.7)
        for x in range(13, 16):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.2, fy=0.2) 
            result = transparentOverlay(cv2_im_processed,charResize,(1282 + ((-13+x) * 90),180),0.7)
        for x in range(16, 19):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.2, fy=0.2) 
            result = transparentOverlay(cv2_im_processed,charResize,(82 + ((-16+x) * 90),511),0.7)
        for x in range(19, 22):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.2, fy=0.2) 
            result = transparentOverlay(cv2_im_processed,charResize,(382 + ((-19+x) * 90),510),0.7)
        for x in range(22, 25):
            characterEntry = app.getOptionBox("Character %d" % x)
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED)
            charResize = cv2.resize(charImg, (0,0), fx=0.2, fy=0.2) 
            result = transparentOverlay(cv2_im_processed,charResize,(682 + ((-22+x) * 90),510),0.7)
        for x in range(25, 28):
            characterEntry = app.getOptionBox("Character %d" % x) 
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED) 
            charResize = cv2.resize(charImg, (0,0), fx=0.2, fy=0.2) 
            result = transparentOverlay(cv2_im_processed,charResize,(982 + ((-25+x) * 90),510),0.7)
        for x in range(28, 31):
            characterEntry = app.getOptionBox("Character %d" % x) 
            charImgString = getCharacterFromEntry(characterEntry) 
            charImg = cv2.imread(charImgString, cv2.IMREAD_UNCHANGED) 
            charResize = cv2.resize(charImg, (0,0), fx=0.2, fy=0.2) 
            result = transparentOverlay(cv2_im_processed,charResize,(1282 + ((-28+x) * 90),510),0.7)
    cv2.imshow("image", result)  
    cv2.imwrite('/Users/Stephen/Documents/Visual Studio Code Workspace/leaderboard.png', result) 
#checks left, right entry boxes to ensure user hasn't input too many characters
def checkUserInput():
    inputLeft = app.getEntry("Left Side Text")
    inputRight = app.getEntry("Right Side Text")
    if len(inputLeft) <= 28 and len(inputRight) <= 25:
        return True  
    elif len(inputLeft) > 28:
        app.errorBox("Too many characters", "Maximum of 28 characters on the left side of image. You have %d" % len(inputLeft))
        return False
    elif len(inputRight) > 25:
        app.errorBox("Too many characters", "Maximum of 25 characters on the right side of image. You have %d" % len(inputRight))
        return False
app.addButton("Create Image", createImage)
app.go()

    

    
    