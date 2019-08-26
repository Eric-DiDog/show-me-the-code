#coding=utf-8
import xlwt
import json

def text2excle(filename):
	with open(filename,'r',encoding='utf-8') as f:
		text=f.read()
		student=json.loads(text)
		print(student)
	workbook = xlwt.Workbook(encoding = 'utf-8')
	# 创建一个worksheet
	worksheet = workbook.add_sheet('student')
	# 写入excel
	# 参数对应 行, 列, 值
	for i,each in enumerate(student) :
		worksheet.write(i,0,i+1)
		j=1
		for per in student[str(i+1)]:
			worksheet.write(i,j,per)
			j+=1
	# 保存
	workbook.save('student.xls')
	
if __name__ == '__main__':
	text2excle('student.txt')
