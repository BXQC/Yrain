from sys import argv
script,input_file = argv#这段是引入文件名
def print_all(f):
	print(f.read())#这个函数是输出文件的内容

def rewind(f):
	f.seek(0,0)#seek(a,b)a指的是开始的偏移量,b有三个值(0,1,2)0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

def print_a_line(line_count,f):
	print(line_count,f.readline())

current_file = open(input_file)
print('First let\'s print the whole file:\n')
print_all(current_file)
print('Now let\'s rewind,kind of like a tape.')
rewind(current_file)#是指针回到开始的位置
print('Let\'s print tree lines:')
current_line = 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

