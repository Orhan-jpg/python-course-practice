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


#syntax of over write
y = open(r"C:\Users\HP\.vscode\python\demo.txt" , "w")
y.write("I am a hero. Consistency is the of success. ")
y.close()

#syntax of append method
y = open(r"C:\Users\HP\.vscode\python\demo.txt" , "a")
y.write(" Then I learn DNS from tomorro inshallah.")
y.write("\nAfter I complete python.")
y.close()

#r+ mode 
y = open(r"C:\Users\HP\.vscode\python\demo.txt" , "r+")
y.write("I am a hero. Consistency is key of success")
print(y.read())
y.close