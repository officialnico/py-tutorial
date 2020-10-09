# Opening files (in python!): 🧙‍♂️

Why do you want to open a file in python? well a lot of data will usually come in files such as the .csv files
this is used to store data and as python programmers we want to manipulate and analyze data, so getting the data from a file 
into a python variable would extremely useful.

Not only does this allow you to read files, but also to <em>write</em> to files as well, which can store the data we give it (i.e variables, strings, data, etc).
  
This can allow your program to store information on your hard drive, unlike variables, this data won't be wiped everytime python is closed.
therefore this is very useful as there is no other <em>relevant</em> way of storing data permanently on your computer in python.

## The open function: `open(filename, permission)`

there are only 2 permissions you have to understand

`'r'` permission for reading the file

`'w'` permission for writing to the file

let's **read** a file, this could be **any** type of file (i.e '.txt', '.csv')

first we have to make sure that the file is in the same folder as the script

for this example let's open and get the data from example filename 'numbers.csv' and lets take that string data (it will always be a string when using open), and put it in a variable.

```
file = open('numbers.csv','r')
text = file.read()
file.close() #important to close file
print(text)
```
always make sure to close your file otherwise you'll get an error: `file.close()` 
