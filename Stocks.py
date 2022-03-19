import os, bs4, requests, tkinter, re, time, random, threading

color_packet = ['AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'alice blue', 'antique white', 'aquamarine', 'aquamarine2', 'aquamarine4', 'azure', 'azure2', 'azure3', 'azure4', 'bisque', 'bisque2', 'bisque3', 'bisque4', 'blanched almond', 'blue', 'blue violet', 'blue2', 'blue4', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadet blue', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate1', 'chocolate2', 'chocolate3', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflower blue', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'cyan2', 'cyan3', 'cyan4', 'dark goldenrod', 'dark green', 'dark khaki', 'dark olive green', 'dark orange', 'dark orchid', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dodger blue', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white', 'forest green', 'gainsboro', 'ghost white', 'gold', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'gray', 'gray1', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray2', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray3', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray4', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray5', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray6', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray7', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray8', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray9', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99', 'green yellow', 'green2', 'green3', 'green4', 'honeydew2', 'honeydew3', 'honeydew4', 'hot pink', 'indian red', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod', 'light goldenrod yellow', 'light grey', 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate blue', 'light slate gray', 'light steel blue', 'light yellow', 'lime green', 'linen', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'navajo white', 'navy', 'old lace', 'olive drab', 'orange', 'orange red', 'orange2', 'orange3', 'orange4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum1', 'plum2', 'plum3', 'plum4', 'powder blue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'red', 'red2', 'red3', 'red4', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandy brown', 'sea green', 'seashell2', 'seashell3', 'seashell4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'sky blue', 'slate blue', 'slate gray', 'snow', 'snow2', 'snow3', 'snow4', 'spring green', 'steel blue', 'tan1', 'tan2', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet red', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white smoke', 'yellow', 'yellow green', 'yellow2', 'yellow3', 'yellow4']
i = 0
namelist = []
pricelist = []
currencylist = []
y_pos = 0
#funkcia na prejdenie urls v text file a zistenie udajov s webu
def Stocks():
    all_companies = open('companyurls.txt', 'r+')
    
    global i
    global currencylist
    global namelist
    global pricelist
    for items in all_companies.readlines():
        i += 1
        items = items.rstrip("\n")
        #print(items)
        requestedwebside = requests.get(items)
        soup = bs4.BeautifulSoup(requestedwebside.text, 'html.parser')
        nameelem = soup.select('.company__name')
        #.company__name
        currencyelem = soup.select('.character')
        #.character
        try:
            priceelem = soup.select('bg-quote.value:nth-child(2)')
            price = priceelem[0].text
            #bg-quote.value:nth-child(2)
        except IndexError:
            priceelem = soup.select('.intraday__price > span:nth-child(2)')
            price = priceelem[0].text
            #.intraday__price > span:nth-child(2)
        currency = currencyelem[0].text
        print(currency)
        name = nameelem[0].text
        print(name)
        price = priceelem[0].text
        namelist.append(name)
        pricelist.append(price)
        currencylist.append(currency)
        print(price)
        print(name, currency, price)
        print(i)
        all_companies.close()
   
Stocks()
#print(currencylist)
#print(namelist)
#print(pricelist)

# GUI create
canvas = tkinter.Tk()
canvas.title('STOCKS')
win_x = 200*i
if win_x > 1600:
    win_x = 1600
canvas=tkinter.Canvas(width=(win_x), height= (200+y_pos),bg='black')
canvas.pack()

# GUI info update
def GUI(event):
    x = 0
    global currencylist
    global namelist
    global pricelist
    global i
    global y_pos
    global canvas
    pos = 0
    y_pos = 0
    #Stocks()
    canvas.delete('all')
    
    for x in range(0,len(namelist)):
        if x == 8:
            pos = 0
            y_pos = 200
        elif x == 16:
            pos = 0
            y_pos = 400
        if len(namelist[(0+x)])> 20:
            name = namelist[(0+x)]
            name.replace(' ' , os.linesep)
            namelist[(0+x)] = name

        canvas.create_rectangle(0 + pos,0 + y_pos,200 + pos,200 + y_pos, fill =color_packet[(0+x)])
        canvas.create_text(100 + pos, 90 + y_pos,text = namelist[(0+x)] , font='arial 14 bold' )
        canvas.create_text(100 + pos, 110 + y_pos,text = pricelist[(0+x)] + '' + currencylist[(0+x)] ,font='arial')
        pos += 200
    canvas.update()
    canvas.pack()
        
    #canvas=tkinter.Canvas(width=(200*i), height= (200+y_pos),bg='black')
    canvas.pack( ipady = (y_pos))  

    currencylist.clear()
    namelist.clear()
    pricelist.clear()
    i = 0
    #print(currencylist, namelist, pricelist)
    #time.sleep(1)
    #GUI()
    #canvas.after(200000, GUI())


    
def add_url(event):
    def show_entry_fields():
        print(e1.get())
        all_companies = open('companyurls.txt', 'a')
        if e1.get != '':
            all_companies.write('\n'+e1.get())
        else:
            pass
        all_companies.close()
        master.destroy()
    master = tkinter.Tk()
    master.title('URL entry')
    master.geometry('250x100')
    tkinter.Label(master,bg ='deep sky blue', text="URL").grid(row=0,column=1)
    e1 = tkinter.Entry(master)
    e1.grid(row=0, column=3,)
    tkinter.Button(master, 
          text='send', command=show_entry_fields).grid(  row=2, 
                                                         column=1, 
                                                         sticky=tkinter.W, 
                                                         pady=4)

    
def recurrsion():
    canvas.bind_all("+", add_url)
    Stocks()
    GUI('a')
    recurrsion()
    
GUI('a')
#recurrsion()
t3 = threading.Thread(target=recurrsion)
t3.start() 
canvas.bind_all("+", add_url)
canvas.bind_all("r", GUI)
tkinter.mainloop()
