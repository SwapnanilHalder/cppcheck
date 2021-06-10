# cppcheck
This is a project, which is created to automate checking a c++ code without entering all the inputs again and again, and check with the expected results. You once provide the inputs and expected correct results, then every time you run this program, it will compile it in a safe directory ~/bin/cpp/ and run it on its own, create an input.txt, output.txt and result.txt file inside ~/bin/cpp/ and check it.  If the output.txt does not match with result.txt, it will say in which line it is differing.


INSTALLING :

run these commands in your terminal:

1. git clone https://github.com/SwapnanilHalder/cppcheck.git
2. cd cppcheck
3. chmod a+x install.sh uninstall.sh
4. ./install.sh

UNINSTALLING :

1. cd cppcheck
2. ./uninstall.sh


Tl;dr
The common pattern of using this program is :

Default => cppcheck <file_name.cpp>

With flag => cppcheck <file_name.cpp> <one flag>


Available flags are :

1. new : restart the program, and provide fresh inputs, expected outputs
2. add : append new inputs and new results onto the previously supplied data
3. edit : edit the inputs and results provided using nano text editor.
4. show : show the contents of input, expected results and output files.


Hi, this is Swapnanil. this script is installing a basic helper
software for hardcore competitive programmers to ease their
task. This is project cppcheck.


In popular competitive programming websites like Codeforces, 
Codechef, Hackerrank, Hackerearth, Atcoder etc. they provide
a set of examples, basic set of inputs and outputs. 


In contests we write a code, try the provided examples, if error happens,
which is most frequently, we try to correct the code, then again
put the inputs and check the outputs. This program is set to automate
this task of giving inputs and outputs and checking repeatatively.


This program will create a folder in your home directory named ~/bin/cpp/
inside 'cpp' folder, everytime you run the program for a .cpp file, 
it will create <file_name> executable file, 'input.txt' , 'output.txt'
and 'result.txt'.


You will be asked to provide the inputs provided by the contest,
and the inputs will be stored inside the 'input.txt' file.
Similarly, you will be asked to provide the expected correct answers
as per the inputs given by the contest, which will be stored inside 
'result.txt' file. This program will 

1. run the desired .cpp file with gcc compiler, 

2. store the <file_name> executable file inside ~/bin/cpp/<file_name> folder, 

3. run it

4. Provide the inputs from 'input.txt' file

5. Store the outputs in 'output.txt' file

6. Compare 'output.txt' file with 'result.txt. file

7. If the context of the files are identical, It will show a \"Correct!!\" prompt

   If not, it will show \"Wrong!!\" prompt and tell you, in which line, it is different

You can use the flags to restart the whole process by deleting all provided
data, append more inputs and expected outputs, or see the input.txt, result.txt,
output.txt file contents, or edit the contents provided using nano text Editor.


If you want to change the default nano text editor by vim, sublime or other you like :
Do change it by going to lib/cppcheck-python.py and change variable default_text_editor
to whatever works for you, be it vim, vi, subl, code 


Some examples :
cppcheck Hello-World.cpp

cppcheck factorial.cpp new

cppcheck factorial.cpp show


END
