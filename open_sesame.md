# Opening files (in python!): 🧙‍♂️

Why do you want to open a file in python? well a lot of data will usually come in files such as .csv files
this is used to store data and as python programmers we want to manipulate and analyze data, so getting data from a file 
into a python variable would be extremely useful.

Not only does this allow you to read files, but also to <em>write</em> to files as well, which can store the data we give it (i.e variables, strings, data, etc).
  
This can allow your program to store information on your hard drive, unlike variables, this data won't be wiped everytime python is closed.
therefore this is very useful as there is no other <em>relevant</em> way of storing data permanently on your computer in python.

## The open function: `open(filename, permission)`

there are only 2 permissions you have to understand

`'r'` permission for reading 📖 the file 

`'w'` permission for writing 🖋 to the file

let's **read** a file, this could be **any** type of file (i.e '.txt', '.csv')

first we have to make sure that the file is in the same folder as the script

for this example let's open and get the data from 'numbers.csv' and lets take that string data (it will always be a string when using open), and put it in a variable.

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

When python is opening this file it's all one big string, no separation,
its up to you to separate the values into lists that you can work with.

## To extract the data from a .csv file! 🌈

Let's clean this csv file [numbers.csv](https://github.com/officialnico/py-tutorial/blob/main/numbers.csv) and extract the data that we want. 

#### 1. Get rid of the ugly space at the bottom 

  `text = text.strip()`

  .strip() is a string function that you can use on any string variable, it will take off any sorrounding empty spaces (i.e "   hi    " turns to "hi")   
  
![](https://imgur.com/c5ewqqZ.jpg)
  
#### 2. Separate the text into different rows

  as you might know new lines in python are represented by the string `"\n"` so you need to use the **`string.split(char)`** function
  
  `rows = text.split("\n")`
  
  ![](https://imgur.com/eQIw71M.jpg)
  
  keep in mind these are strings we need to split those even further
  
#### 3. Separate the each row in the list rows by the commas

  ###### len() function: aka length
  `len(rows)` will return the amount of elements in said list (in this case 2)
  
  `len("random string")` will return the number of characters in that string
  
  in conclusion: len() is a useful function for finding the length of things, specially useful when dealing with `range()` in for loops
  the reason why i used the range function was because it was easier to understand in this case and easy to manipulate the elements based on index,
  this is good when you want to take some element, modify it, and **replace** the element previously in it's place 👌 
  
  ###### using len() in a range(start, finish) for loop:
 this is needed in our case of splitting every element up by the comma, but still keeping it in the 'rows' list
  ```
  for i in range(0,len(rows)):
    rows[i]=rows[i].split(',')
  ```

  
![](https://imgur.com/apYlBkL.jpg) 
  
#### 4. Create a nested for loop to go through each element in rows

  ```
  for row in rows:
    for element in row:
      print(element)
  ```
  this will go through every element of every list stored in rows, this is one of the most important programming concepts
  it might seem intimidating but it's a life hack once you understand it
  
#### 5. Conclusion: 

to bring it all together your final code should look like this

```
file = open('numbers.csv','r')
text = file.read()
file.close() #important to close the file after reading

text = text.strip()

rows = text.split("\n")

for i in range(0,len(rows)):
  rows[i]=rows[i].split(',')
    
for row in rows:
  for element in row:
    print(element)
```
![](https://imgur.com/wkeHsfo.jpg) 

keep in mind these numbers are still strings, when we go to compare them later we will have to deal with this by using `float()`

currently:
`rows==[['22', '36', '82', '20'], ['89', '21', '23', '134']]`

## The `list.index(element)` Function:
this will return the index of element in list
Keep this in mind for later as it's useful for replacing values
in this case:

`1 == rows.index(['89', '21', '23', '134'])`
 
## Ex. Pick only the grades over 65, and put their position (index) in a list corresponding to the grade's list, and take the name of the csv file as a [command line argument](https://github.com/officialnico/py-tutorial/blob/main/README.md#how-to-get-arguments-from-the-terminal-command-line) 

input (numbers.csv): 
[![watch](https://imgur.com/ADYR9OJ.jpg)](https://github.com/officialnico/py-tutorial/blob/main/numbers.csv)

output:
```
[0,1,3]
[1,2]
```

[answer](https://github.com/officialnico/py-tutorial/blob/main/school_grades.py)


 
  
