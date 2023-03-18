"""
'w' = Write Only Mode
'r' = Read Only Mode
'r+' = Read and Write Mode
'a' = Append (add) Mode
"""
# This is Normal File Write/Read #
"""
print("Normal File Write")
my_write = open('filetext.txt', 'w')
my_write.write("Trying to write to this file")
my_write.close()

my_read = open('filetext.txt', 'r')
print(my_read.read())
"""

# Read and Write with WITH and AS
# This way, you don't need to worry about Closing the file
# write.close()

print("Using \'With' keyword to Write/Read")

with open('withfile.txt', 'w') as with_as_write:
    with_as_write.write("This text is going to write into this File")

print("Using \'AS' keyword to Write/Read")
with open('withfile.txt', 'r') as with_as_read:
    print(with_as_read.read())




