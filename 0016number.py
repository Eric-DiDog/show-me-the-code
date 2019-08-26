#coding=utf-8
import xlwt
import json

def text2excle(filename):
	with open(filename,'r',encoding='utf-8') as f:
		text=f.read()
		number=eval(text)
		print(number)
	workbook = xlwt.Workbook(encoding = 'utf-8')
	# # 创建一个worksheet
	worksheet = workbook.add_sheet('number')
	# # 写入excel
	# # 参数对应 行, 列, 值
	for i,each in enumerate(number) :
		for j,data in enumerate(each):
			worksheet.write(i,j,data)
	workbook.save('number.xls')
	

if __name__ == '__main__':
	text2excle('numbers.txt')
