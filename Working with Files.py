"""
'w' = Write Only Mode
'r' = Read Only Mode
'r+' = Read and Write Mode
'a' = Append (add) Mode
"""

myList = [1, 2, 3, 4, 5]

# my_file = open("firstfile.txt", "w")   # this is to Write into File
my_file = open("firstfile.txt", "r")     # this is to Read the File

print(my_file.read())
"""For loop is to Write the File """
# for i in myList:
#    my_file.write(str(i) + "\n")
print("Reading One Line at a time ==================")

# Ready Multiple lines at a time
my_file_line = open("firstfile.txt", "r")
print(my_file_line.readline())
print(my_file_line.readline())

my_file.close()
