from file import File

file1 = File('test1.txt')
file2 = File('test2.txt')
file1.write('String for test1')
file2.write('String for test2')

new_file = file1 + file2

print(file1)
print(file2)
print(new_file)

file1.read()
file2.read()

new_file.read()

import os.path
os.path.exists(r'C:\Users\Media\AppData\Local\Temp\new_file_from_test1.txt_and_test2.txt')