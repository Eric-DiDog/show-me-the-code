from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import random
import string
def get_randcolor():
	c1=random.randint(0,255)
	c2=random.randint(0,255)
	c3=random.randint(0,255)
	return (c1,c2,c3)

def get_randstr():
	str=''
	char_set=string.ascii_letters + string.digits
	for i in range(1,5):
		# if random.randint(1,5)<3:
		# 	str+=' '
		str+=random.choice(char_set)
	return str

def identify_code(name):
	
	img=Image.new('RGB',(200,80),get_randcolor())
	draw = ImageDraw.Draw(img)
	font=ImageFont.truetype("verdana.ttf",size=45)
	str=get_randstr()
	draw.text((0,0),str,get_randcolor(),font=font)
	for i in range(4):
		x1=random.randint(0,img.width)
		x2=random.randint(0,img.width)
		y1=random.randint(0,img.height)
		y2=random.randint(0,img.height)
		draw.line((x1,y1,x2,y2),fill=get_randcolor())
	for i in range(20):
		draw.point([random.randint(0, img.width), random.randint(0, img.height)], fill=get_randcolor())
	img.save(open('%s.png'%name,'wb'),'png')
	return (img,str)



if __name__ == '__main__':
	img,code= identify_code('test')
	img.show()
	print(code)