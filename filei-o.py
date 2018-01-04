my_output_file = open("hello.txt", "a")

lines_to_write = ["This is my file",
                  "\n there are many like it,",
                  "\n but this one is mine.\n"]

my_output_file.writelines(lines_to_write)
my_output_file.close()

my_input_file = open("hello.txt", "r")

line = my_input_file.readline()
while line != "":
    print(line)
    line = my_input_file.readline()

my_input_file.close()
