import sys
import os

#Remember the problem we were having before where no directory is found?
#ill show you how to fix that

#you want to change this file's working directory to the one where the file is located 
#(ik its crazy but the script has a variable called __file__ which is set when you first make the file as the directory),
#and we have to change that to our current directory
#Whenever you have this issue of: No such file or directory: 'numbers.csv'
#make sure to enter the following code to change the directory to the script directory whenever working with open()

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

#make sure to have numbers.csv in the same folder
#run like this:
#python nested.py numbers.csv 

### Program ###

#Opens the csv file and stores the text
filename = sys.argv[1] #takes command line argument 
file = open(filename,'r') 
text = file.read()
file.close()

#Strips away the sorrounding spaces
text = text.strip()

#Splits the text into it's corresponding rows
rows = text.split("\n")
#rows == [['22,36,82,20'],['89,21,23,134']]

#Splits rows by their commas and stores them back in the same place
for i in range(0,len(rows)):
  rows[i]=rows[i].split(',')
#rows == [['22', '36', '82', '20'], ['89', '21', '23', '134']]

##let's convert the strings to floats
for row in rows:
  for element in row:
    current_row_i = rows.index(row)
    current_element_i = row.index(element)
    rows[current_row_i][current_element_i] = float(element)

big_list = []
for row in rows: 
  small_list = [] #small list resets every time
  for element in row:
    if(element<65): #grading limit
      small_list.append(row.index(element)) #list.index(element) will return the index of that element
  big_list.append(small_list) #now you append small_list to big_list which unlike small_list, doesn't reset
#big_list == [[0,1,3],[1,2]]

#Now print the elements (lists) inside big_list (in this case the 2 lists)
for l in big_list:
  print(l)
  
#Output:
#[0, 1, 3]
#[1, 2]

#Note: there is no right answer in coding, you just throw it at the wall and see what sticks,
#if this seems less than simple try making it yourself it seems a lot simpler when you write it :) 
#you are intelligent, kind, courageous, and curious, you got this!
