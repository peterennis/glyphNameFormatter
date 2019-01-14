size(1600,451)
for n in installedFonts():
    if n.find("Microgramma")!=-1:
        print(n)

ss = 188
ss2 = 132
ss3 = 177.4
f = 0.74
f2 = 0.8
fill(1,.5,.2)
rect(0,0,width(), height())
fill(1)
fontSize(ss)
font("MicrogrammaCom-BoldExtended")
text("GLYPHNAME", (10,height()-140))
text("FORMATTER", (10,height()-280))
fontSize(ss2)
fill(.4,.3,.4,.3)
text("unicode11", (10,20))

saveImage("banner.png")
saveImage("banner.svg")