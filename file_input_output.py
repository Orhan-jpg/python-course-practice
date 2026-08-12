#syntax of writting file input & output
f = open(r"C:\Users\HP\.vscode\python\demo.txt" , "r")
file = f.read()
print(file)
f.close()

y = open(r"C:\Users\HP\.vscode\python\demo.txt" , "r")
line1 = y.readlines()
print(line1)

line2 = y.readlines()
print(line2)
y.close()