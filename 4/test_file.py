from file import File

file1 = File('/domains/test1.txt')
file2 = File('/domains/test2.txt')
file1.write('String for test1\nsecond\nstr')
file2.write('String for test2')

new_file = file1 + file2

print(file1)
print(file2)
print(new_file)

print(file1.read())
print(file2.read())

print(new_file.read())

for line in new_file:
    print(f"line:{line}")