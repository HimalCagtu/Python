import googletrans
from googletrans import  Translator
inp = input("Please Enter a sentance")
trans = Translator()
trans.translate(inp,src="en",dest="np")
