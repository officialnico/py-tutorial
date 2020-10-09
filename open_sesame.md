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
always make sure to close your file otherwise you'll get an error 

this is what the file looks like opened with your mac TextEdit
![](https://imgur.com/cf4gf9j.jpg)

and this is what it looks like when we run this code above:
![](https://imgur.com/2fSSkzW.jpg)

Now you gotta take in when python is getting this its all one big string, no separation, its up to you to do that.

Let's clean this and extract the data that we want. 

1. Get rid of the ugly space at the bottom 

`text = text.strip()`

 strip is a string function that you can use on any string variable of your, just like `st.lower()`
 
 `st.strip()`  will get rid of any spaces on the outsides of the string
