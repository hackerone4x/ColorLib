import random
class ColorsLib:
    def __init__(self) -> None:
        """
            -------------------------------------
            # Colors Library
            -------------------------------------
            Standered Colors Library For Python3
            -------------------------------------
            * VERSION = [1.1]
            -------------------------------------
            * [ENG:Abdulrahman Ayman][@hackerone4x]
            ----------------------------------------"""
        self.PackageInformation = '[ENG:Abdulrahman Ayman][@hackerone4x][V(1.1)]'
        # ColornameVar = [Colorname , HexCode , RGB Color Format]
        self.RedColor = ['Red','FF0000',(255, 0, 0),0]
        self.GreenColor = ['Green','008000' ,(1, 128, 0),1]
        self.BlueColor = ['Blue','0000FF',(0, 0, 255),2]
        self.WhiteColor =  ['White','FFFFFF',(255,255,255),3]
        self.IvoryColor = ['Ivory','FFFFF0' ,(255, 255, 240),4]
        self.BlackColor = ['Black','000000' , (0,0,0),5]
        self.GrayColor = ['Gray','808080' ,(128, 128, 128),6]
        self.SilverColor = ['Silver','C0C0C0' ,(192, 192, 192),7]
        self.YellowColor = ['Yellow','FFFF00' ,(255, 255, 0),8]
        self.PurpleColor = ['Purple','800080' ,(128, 0, 128),9]
        self.OrangeColor = ['Orange','FFA500' ,(255, 165, 0),10]
        self.MaroonColor = ['Maroon','800000' ,(128, 0, 0),11]
        self.FuchsiaColor = ['Fuchsia','FF00FF' ,(255, 0, 255),12]
        self.LimeColor = ['Lime','00FF00' ,(0, 255, 0),13]
        self.Aqua = ['Aqua','00FFFF' ,(0, 255, 255),14]
        self.TealColor = ['Teal','008080' ,(0, 128, 128),15]
        self.OliveColor = ['Olive','808000' ,(128, 128, 0),16]
        self.NavyColor = ['Navy','000080' ,(0, 0, 128),17]
        self.MainColors = ['Red', 'Green', 'Blue','White', 'Ivory', 'Black', 'Gray', 'Silver','Yellow', 'Purple', 'Orange', 'Maroon', 'Fuchsia', 'Lime', 'Aqua', 'Teal', 'Olive', 'Navy']
        self.Colors = ['Red', 'Green', 'Blue', 'White', 'Ivory', 'Black', 'Gray', 'Silver', 'Yellow', 'Purple', 'Orange', 'Maroon', 'Fuchsia', 'Lime', 'Aqua', 'Teal', 'Olive', 'Navy', 'Mred','Mpink', 'Mpurple', 'MdeepPurple', 'Mindigo', 'Mblue', 'MlightBlue', 'Mcyan', 'Mteal', 'Mgreen', 'MlightGreen', 'Mlime', 'Myellow', 'Mamber', 'Morange', 'MdeepOrange', 'Mbrown', 'Mgray', 'MblueGray']
        # f44336	rgb(244, 67, 54)	Red
        # e81e63	rgb(232, 30, 99)	Pink
        # 9c27b0	rgb(156, 39, 176)	Purple
        # 673ab7	rgb(103, 58, 183)	Deep Purple
        # 3f51b5	rgb(63, 81, 181)	Indigo
        # 2196f3	rgb(33, 150, 243)	Blue
        # 03a9f4	rgb(3, 169, 244)	Light Blue
        # 00bcd4	rgb(0, 188, 212)	Cyan
        # 009688	rgb(0, 150, 136)	Teal
        # 4caf50	rgb(76, 175, 80)	Green
        # 8bc34a	rgb(139, 195, 74)	Light Green
        # cddc39	rgb(205, 220, 57)	Lime
        # ffeb3b	rgb(255, 235, 59)	Yellow
        # ffc107	rgb(255, 193, 7)	Amber
        # ff9800	rgb(255, 152, 0)	Orange
        # ff5722	rgb(255, 87, 34)	Deep Orange
        # 795548	rgb(121, 85, 72)	Brown
        # 9e9e9e	rgb(158, 158, 158)	Gray
        # 607d8b	rgb(96, 125, 139)	Blue Gray
        self.Mred = ['red','F44336',(244,67,54),18] # 18
        self.Mpink = ['pink', 'e81e63', (232, 30, 99),19]
        self.Mpurple = ['purple', '9c27b0', (156, 39, 176),20]
        self.Mdeep_Purple = ['deepPurple', '673ab7', (103, 58, 183),21]
        self.Mindigo = ['indigo', '3f51b5', (63, 81, 181),22]
        self.Mblue = ['blue', '2196f3', (33, 150, 243),23]
        self.Mlight_Blue = ['lightBlue', '03a9f4', (3, 169, 244),24]
        self.Mcyan = ['cyan', '00bcd4', (0, 188, 212),25]
        self.Mteal = ['teal', '009688', (0, 150, 136),26]
        self.Mgreen = ['green', '4caf50', (76, 175, 80),27]
        self.Mlight_Green = ['lightGreen', '8bc34a', (139, 195, 74),28]
        self.Mlime = ['lime', 'cddc39',(205, 220, 57),29]
        self.Myellow = ['yellow', 'ffeb3b', (255, 235, 59),30]
        self.Mamber = ['amber', 'ffc107', (255, 193, 7),31]
        self.Morange = ['orange', 'ff9800', (255, 152, 0),32]
        self.Mdeep_Orange = ['deepOrange', 'ff5722', (255, 87, 34),33]
        self.Mbrown = ['brown', '795548', (121, 85, 72),34]
        self.Mgray = ['gray', '9e9e9e', (158, 158, 158),35]
        self.Mblue_Gray = ['blueGray', '607d8b', (96, 125, 139),36]
        self.MaterialColors = ['Mred', 'Mpink','Mpurple', 'MdeepPurple', 'Mindigo', 'Mblue', 'MlightBlue', 'Mcyan', 'Mteal', 'Mgreen', 'MlightGreen', 'Mlime', 'Myellow', 'Mamber', 'Morange', 'MdeepOrange', 'Mbrown', 'Mgray', 'MblueGray']
        self.Hex0xList = ['0', '1', '2', '3', '4', '5', '6','7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        self.id_names = {0: 'FF0000', 1: '008000',
                        2: '0000FF',
                        3: 'FFFFFF', 
                        4: 'FFFFF0', 
                        5: '000000',
                        6: '808080',
                        7: 'C0C0C0',
                        8: 'FFFF00',
                        9: '800080',
                        10: 'FFA500',
                        11: '800000',
                        12: 'FF00FF',
                        13: '00FF00',
                        14: '00FFFF',
                        15: '008080',
                        16: '808000',
                        17: '000080',
                        18: 'F44336',
                        19: 'e81e63',
                        20: '9c27b0',
                        21: '673ab7',
                        22: '3f51b5',
                        23: '2196f3',
                        24: '03a9f4',
                        25: '00bcd4',
                        26: '009688',
                        27: '4caf50',
                        28: '8bc34a',
                        29: 'cddc39',
                        30: 'ffc107',
                        31: 'ffc107',
                        32: 'ff9800',
                        33: 'ff5722',
                        34: '795548',
                        35: '9e9e9e',
                        36: '607d8b'}
        self.PURPLE = '\033[95m'
        self.CYAN = '\033[96m'
        self.DARKCYAN = '\033[36m'
        self.BLUE = '\033[94m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.RED = '\033[91m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.END = '\033[0m'
        self.AlpaPoint = 256
        self.TermColors = {
            'PURPLE' : '\033[95m',
            'CYAN' : '\033[96m',
            'DARKCYAN' : '\033[36m',
            'BLUE' : '\033[94m',
            'GREEN' : '\033[92m',
            'YELLOW' : '\033[93m',
            'RED' : '\033[91m'
        }
        self.style = {
            'BOLD' : '\033[1m',
            'UNDERLINE' : '\033[4m',
            'END' : '\033[0m'
        }
    def RandomMakerPY():
        Dt0 = "\033["
        Dt1 = random.randint(0,5)
        Dt2 = random.randint(0,32)
        Dt3 = random.randint(0,30)
        Dt = str(Dt0+str(Dt1)+";"+str(Dt2)+";"+str(Dt3)+"m")
        return Dt
    def HexRandomColorMaker():
        ColorHex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        C1 = ColorHex[random.randint(0,15)]
        C2 = ColorHex[random.randint(0,15)]
        C3 = ColorHex[random.randint(0,15)]
        C4 = ColorHex[random.randint(0,15)]
        C5 = ColorHex[random.randint(0,15)]
        C6 = ColorHex[random.randint(0,15)]
        return f'{C1}{C2}{C3}{C4}{C5}{C6}'
    def convertHexToDec(self,Hex : str):
        if len(Hex) >= 1:
            Index = len(Hex)-1
            HexListCh = []
            res = 0
            for i in Hex:
                HexListCh.append(i)
            for i in HexListCh:
                if i in self.Hex0xList:
                    res += (int(self.Hex0xList.index(i))*(16**Index))
                    Index -= 1
                else:
                    print(f'{i} Is*t In HexList')
            return res
        else:
            return 0
    def convertDectoHex(self,Dec : int):
        HexL = []
        Strp = ''
        for i in hex(Dec)[1:]:
            HexL.append(i)
        ixl = HexL.index('x')
        for c in HexL[ixl+1:]:
            Strp += str(c)
        return str(Strp)
    def rgb(self,Red: int = 0,Green : int = 0 , Blue : int = 0):
        if (Red in range(256)) and (Green in range(256)) and (Green in range(256)):
            ColorRed = self.convertDectoHex(Red)
            ColorGreen = self.convertDectoHex(Green)
            ColorBlue = self.convertDectoHex(Blue)
            if len(ColorRed) == 1:
                ColorRed = str("0"+ColorRed)
            if len(ColorGreen) == 1:
                ColorGreen = str("0"+ColorGreen)
            if len(ColorBlue) == 1:
                ColorBlue = str("0"+ColorBlue)
            return f'{ColorRed}{ColorGreen}{ColorBlue}'
        else:
            return False
    def rgba(self, Red: int = 0, Green: int = 0, Blue: int = 0, Alpha: int = 1):
        if (Red in range(256)) and (Green in range(256)) and (Green in range(256)):
            ColorRed = self.convertDectoHex(Red)
            ColorGreen = self.convertDectoHex(Green)
            ColorBlue = self.convertDectoHex(Blue)
            if len(ColorRed) == 1:
                ColorRed = str("0"+ColorRed)
            if len(ColorGreen) == 1:
                ColorGreen = str("0"+ColorGreen)
            if len(ColorBlue) == 1:
                ColorBlue = str("0"+ColorBlue)
            AlphaColor = int(float(Alpha)*float(self.AlpaPoint))
            Alphares = self.convertDectoHex(AlphaColor)
            return f'{ColorRed}{ColorGreen}{ColorBlue}{Alphares}'
        else:
            return False
    def UseColor(self,ColorName : str,Id : int):
        if (ColorName) or (Id):
            if ColorName:
                if ColorName in self.Colors:
                    indexofColor = self.Colors.index(ColorName)
                    HexColor = self.id_names[indexofColor]
                    return HexColor
                else:
                    return False
            elif Id:
                try:
                    return self.id_names[Id]
                except:
                    return False
            else:
                return False
        else:
            return False
