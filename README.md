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
  
![Imgur](https://imgur.com/8w9xQSq)
  
  

### Passing arguments through the terminal
```
import sys
sys.argv[1]  

```
