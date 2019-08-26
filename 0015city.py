#coding=utf-8
import xlwt
import json

def text2excle(filename):
	with open(filename,'r',encoding='utf-8') as f:
		text=f.read()
		city=json.loads(text)
		print(city)
	workbook = xlwt.Workbook(encoding = 'utf-8')
	# 创建一个worksheet
	worksheet = workbook.add_sheet('city')
	# 写入excel
	# 参数对应 行, 列, 值
	for i,each in enumerate(city) :
		worksheet.write(i,0,i+1)
		worksheet.write(i,2,city[str(i+1)])
	workbook.save('city.xls')
	
if __name__ == '__main__':
	text2excle('city.txt')
