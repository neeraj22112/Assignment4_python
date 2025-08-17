writing_input = input("Enter text to write to the flie: ")
file1=open('output.txt','w')
file1.write(writing_input + "\n")
file1.close()

append_input = input("Enter additional text to append: ")
file1=open('output.txt','a')
file1.write(append_input + "\n")
file1.close()

file1 = open('output.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()