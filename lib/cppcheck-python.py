import os
import sys
import subprocess
import filecmp

default_text_editor = "nano" # options : vim, vi, subl, code, nano

flag = ""
if(len(sys.argv) == 3) :
    flag = sys.argv[2]

path = sys.argv[1]
path = path[:-4]

for i in range(len(path)-1, -1, -1) :
    if (path[i] == '/'):
        file_name = path[(i+1):]
        break

home = os.path.expanduser('~')
in_out = home +'/bin/cpp/' + file_name+ '/'
input_file = in_out + 'input.txt'
output_file = in_out + 'output.txt'
result_file = in_out + 'result.txt'

if (flag == "new") :
    os.system("rm -rf " + in_out)

elif (flag == 'add') :
    print("Enter Extra Input : (Press ctrl+d to Exit)")
    os.system("cat "+ '>> '+ input_file)
    print("Enter Extra Correct Answer : (Press Enter to register the line of answer) ")
    os.system("cat "+ '>> '+ result_file)

elif (flag == 'edit') :
    os.system(default_text_editor + " "+input_file)
    os.system(default_text_editor + " "+result_file)

elif (flag == 'show') :
    os.system("echo Input File :")
    os.system("cat "+input_file)
    print()
    os.system("echo Expected Answer :")
    os.system("cat "+result_file)
    print()
    os.system("echo Answer Got :")
    os.system("cat "+output_file)
    exit()
else :
    print("Available flags are : new, add, show, edit")
    exit()


if (os.path.isdir(in_out) == False) :
    os.system('mkdir -p'+ in_out)
    print("Enter Input : (Press ctrl+d to Exit)")
    os.system("touch " + input_file)
    os.system("cat "+ '> '+ input_file)
    print("Enter Correct Answer : (Press Enter to register the line of answer) ")
    os.system("touch "+ result_file)
    os.system("cat "+ '> '+ result_file)
    


os.system("g++ "+ path + ".cpp -o ~/bin/cpp/" + file_name+ "/"+file_name)

print()
 
os.system(in_out+file_name+'<'+input_file+'>'+output_file)
result = filecmp.cmp(output_file, result_file, shallow=False)
if(result == True) :
    print("Correct!!")
else :
    print("Wrong!!")
    f1 = open(result_file, "r")
    f2 = open(output_file, "r")
    count_f1 = 0
    count_f2 = 0
    for _ in f1 :
        count_f1 += 1
    for _ in f2 : 
        count_f2 += 1
    if (count_f1 > count_f2) :
        print("You are outputting less no. of lines than expected")
    if (count_f1 < count_f2) :
        print("You are outputting more no. of lines than expected")
    i = 0
    for line1 in f1:
        i += 1
        for line2 in f2:
            if line1 != line2 :
                print("Line ", i, ":")
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
    f1.close()
    f2.close()
