from sys import argv # 将python的模块导入脚本

script, filename = argv #将argv解包

txt = open(filename) #打开ex15_sample.txt文件并将值赋予给txt变量

print "Here is your file: %r." % filename
print txt.read () # 执行txt的read属性

print "Type the filename again:"
file_again = raw_input (">") # 输入文件名

txt_again = open(file_again) #打开这个文件并将值赋予给txt_again这个变量

print txt_again.read() # 执行txt_again read属性
