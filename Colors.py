import random
class Colors:
    #values from https://en.wikipedia.org/wiki/Web_colors#X11_color_names

    # PINK COLORS
    PINK               = (255,192,203)
    LIGHTPINK          = (255,182,193)
    HOTPINK            = (255,105,180)
    DEEPPINK           = (255,20,147)
    PALEVIOLETRED      = (219,112,147)
    MEDIUMVIOLETRED    = (199,21,133)
    # RED COLORS
    LIGHTSALMON        = (255,160,122)
    SALMON             = (250,128,114)
    DARKSALMON         = (233,150,122)
    LIGHTCORAL         = (240,128,128)
    INDIANRED          = (205,92,92)
    CRIMSON            = (220,20,60)
    FIREBRICK          = (178,34,34)
    DARKRED            = (139,0,0)
    RED                = (255,0,0)
    # ORANGE COLORS
    ORANGERED          = (255,69,0)
    TOMATO             = (255,99,71)
    CORAL              = (255,127,80)
    DARKORANGE         = (255,140,0)
    ORANGE             = (255,165,0)
    # YELLOW COLORS
    YELLOW             = (255,255,0)
    LIGHTYELLOW        = (255,255,224)
    LEMONCHIFFON       = (255,250,205)
    LIGHTGOLDENRODYELLOW= (250,250,210)
    PAPAYAWHIP         = (255,239,213)
    MOCCASIN           = (255,228,181)
    PEACHPUFF          = (255,218,185)
    PALEGOLDENROD      = (238,232,170)
    KHAKI              = (240,230,140)
    DARKKHAKI          = (189,183,107)
    GOLD               = (255,215,0)
    # BROWN COLORS
    CORNSILK           = (255,248,220)
    BLANCHEDALMOND     = (255,235,205)
    BISQUE             = (255,228,196)
    NAVAJOWHITE        = (255,222,173)
    WHEAT              = (245,222,179)
    BURLYWOOD          = (222,184,135)
    TAN                = (210,180,140)
    ROSYBROWN          = (188,143,143)
    SANDYBROWN         = (244,164,96)
    GOLDENROD          = (218,165,32)
    DARKGOLDENROD      = (184,134,11)
    PERU               = (205,133,63)
    CHOCOLATE          = (210,105,30)
    SADDLEBROWN        = (139,69,19)
    SIENNA             = (160,82,45)
    BROWN              = (165,42,42)
    MAROON             = (128,0,0)
    # GREEN COLORS
    DARKOLIVEGREEN     = (85,107,47)
    OLIVE              = (128,128,0)
    OLIVEDRAB          = (107,142,35)
    YELLOWGREEN        = (154,205,50)
    LIMEGREEN          = (50,205,50)
    LIME               = (0,255,0)
    LAWNGREEN          = (124,252,0)
    CHARTREUSE         = (127,255,0)
    GREENYELLOW        = (173,255,47)
    SPRINGGREEN        = (0,255,127)
    MEDIUMSPRINGGREEN  = (0,250,154)
    LIGHTGREEN         = (144,238,144)
    PALEGREEN          = (152,251,152)
    DARKSEAGREEN       = (143,188,143)
    MEDIUMAQUAMARINE   = (102,205,170)
    MEDIUMSEAGREEN     = (60,179,113)
    SEAGREEN           = (46,139,87)
    FORESTGREEN        = (34,139,34)
    GREEN              = (0,128,0)
    DARKGREEN          = (0,100,0)
    # CYAN COLORS
    AQUA               = (0,255,255)
    CYAN               = (0,255,255)
    LIGHTCYAN          = (224,255,255)
    PALETURQUOISE      = (175,238,238)
    AQUAMARINE         = (127,255,212)
    TURQUOISE          = (64,224,208)
    MEDIUMTURQUOISE    = (72,209,204)
    DARKTURQUOISE      = (0,206,209)
    LIGHTSEAGREEN      = (32,178,170)
    CADETBLUE          = (95,158,160)
    DARKCYAN           = (0,139,139)
    TEAL               = (0,128,128)
    # BLUE COLORS
    LIGHTSTEELBLUE     = (176,196,222)
    POWDERBLUE         = (176,224,230)
    LIGHTBLUE          = (173,216,230)
    SKYBLUE            = (135,206,235)
    LIGHTSKYBLUE       = (135,206,250)
    DEEPSKYBLUE        = (0,191,255)
    DODGERBLUE         = (30,144,255)
    CORNFLOWERBLUE     = (100,149,237)
    STEELBLUE          = (70,130,180)
    ROYALBLUE          = (65,105,225)
    BLUE               = (0,0,255)
    MEDIUMBLUE         = (0,0,205)
    DARKBLUE           = (0,0,139)
    NAVY               = (0,0,128)
    MIDNIGHTBLUE       = (25,25,112)
    # PURPLE, VIOLET, AND MAGENTA COLORS
    LAVENDER           = (230,230,250)
    THISTLE            = (216,191,216)
    PLUM               = (221,160,221)
    VIOLET             = (238,130,238)
    ORCHID             = (218,112,214)
    FUCHSIA            = (255,0,255)
    MAGENTA            = (255,0,255)
    MEDIUMORCHID       = (186,85,211)
    MEDIUMPURPLE       = (147,112,219)
    BLUEVIOLET         = (138,43,226)
    DARKVIOLET         = (148,0,211)
    DARKORCHID         = (153,50,204)
    DARKMAGENTA        = (139,0,139)
    PURPLE             = (128,0,128)
    INDIGO             = (75,0,130)
    DARKSLATEBLUE      = (72,61,139)
    SLATEBLUE          = (106,90,205)
    MEDIUMSLATEBLUE    = (123,104,238)
    # WHITE COLORS
    WHITE              = (255,255,255)
    SNOW               = (255,250,250)
    HONEYDEW           = (240,255,240)
    MINTCREAM          = (245,255,250)
    AZURE              = (240,255,255)
    ALICEBLUE          = (240,248,255)
    GHOSTWHITE         = (248,248,255)
    WHITESMOKE         = (245,245,245)
    SEASHELL           = (255,245,238)
    BEIGE              = (245,245,220)
    OLDLACE            = (253,245,230)
    FLORALWHITE        = (255,250,240)
    IVORY              = (255,255,240)
    ANTIQUEWHITE       = (250,235,215)
    LINEN              = (250,240,230)
    LAVENDERBLUSH      = (255,240,245)
    MISTYROSE          = (255,228,225)
    # GRAY AND BLACK COLORS
    GAINSBORO          = (220,220,220)
    LIGHTGRAY          = (211,211,211)
    SILVER             = (192,192,192)
    DARKGRAY           = (169,169,169)
    GRAY               = (128,128,128)
    DIMGRAY            = (105,105,105)
    LIGHTSLATEGRAY     = (119,136,153)
    SLATEGRAY          = (112,128,144)
    DARKSLATEGRAY      = (47,79,79)
    BLACK              = (0, 0, 0)



    @staticmethod
    def darkenColor(color, amount=0.875):
        return tuple([value*amount for value in color])

    @staticmethod
    def lightenColor(color, amount=0.875):
        return tuple([(value-255)*amount+255 for value in color])


    @staticmethod
    def randColor(lowBound=0, highBound=255):
        return tuple([random.randint(lowBound, highBound) for times in range(3)])

    @classmethod
    def randDarkColor(cls):
        return cls.randColor(0,130)

    @classmethod
    def randLightColor(cls):
        return cls.randColor(110, 200)

    @classmethod
    def randReallyLightColor(cls):
        return cls.randColor(200,250)
