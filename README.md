# Python Notes 🌁

## How to get arguments from the terminal (command line):

### What are arguments? Arguments are what you passing to functions in the parentheses ():
`print(arg1)`
or more generically
`function(arg1,arg2,arg3)`

### Why do we need to get arguments from the terminal?
  Passing arguments through the command line can be very useful because
  then you don't have to ask the user for input.
  Think about it, do you want to be asked for input everytime? 
  
### Passing arguments through input() (the usual way): 
```
x = input("enter number: ")
print(x)
```

![using input()](https://i.imgur.com/VHa4Ujo.png)

### sys
  sys (system) is a python library that will help you in performing system related tasks,
  usually this involves interacting with the terminal. 
  Since it's a library you have to import it.
  put this at the top of your code:
  `import sys`
  

### sys.argv 
  sys.argv is an array of all the arguments given at the command line,
  the first argument is always the filename
 
```
import sys
print(sys.argv)
```
  
![Imgur](https://i.imgur.com/8w9xQSq.jpg)
  
in this example 
```
arg1 == sys.argv[1]
arg2 == sys.argv[2]
arg3 == sys.argv[3]
```
 

### Passing one argument through the terminal
most of the time you will want to take one argument so all you need to do is this:
```
import sys
x = sys.argv[1]  
```
store it in a variable (in this case x) and use it as the input.
Examples of this input could be a integer, string, float... anything can be passed as an argument,
it's up to you what you use that 'data' for.

#### "equals equals" aka `==`
1==1 is true
1==2 is false
'==' is just telling you whether the two items are equal instead of '=' which will assign it a value (i.e x='apples' vs x=='apples')

### Notes:
* terminal arguments are useful because we don't have to ask the user for input(), taking up time.
* libraries are python's way of storing functions so that we don't have to
* sys is a library used for interacting with the system and terminal


