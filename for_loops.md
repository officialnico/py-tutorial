# for loops 🏔☯️


they sound scary but for loops are the best thing ever, I'm going to try to convince you

so say you have a list 'a' of any number (or type) of elements

`a = ["elm1", "elm2", "elm3"]`

Try to print every single one of those elements like this

![imgur](https://imgur.com/P21TLAT.jpg)

i'll wait 😌

if you notice a problem, you might be onto something because there is one!

You have to cycle through these elements to print them pretty... but how?

Use a for loop! anytime you're asked to cycle through a list for loops are the way to go!

look how easy and efficient this is

```
a = ["elm1", "elm2", "elm3"]

for x in a:
  print(x)
```

output: 

![imgur](https://imgur.com/P21TLAT.jpg)

#### how `for x in a:` reads:	
"for every element in a `["elm1", "elm2", "elm3"]`
assign one to x and then run the following code `print(x)`, afterwards go to the next element"	


#### illustration:
![](https://i.imgur.com/91NoaP0.jpg)

(iterate means "to cycle through", we iterate 'over' lists)

## Range function: `range(start, finish)`

the range functions is how most people first learn to use for loops because of how easy it is.

The range function is simple: you say what index you wish to start at, and which one to end at.

This is useful because if you know you want to run your for loop only, lets say, 5 times--then you can.
the range function will bring you the list of numbers from your start to finish.

```
r = range(0,5)
print(r)
```
![](https://imgur.com/84xHYVf.jpg)

therefore, in this case `range(0,5)==[0,1,2,3,4]`

For a lot of problems you'll have to make a loop that only cycles a certain number of times if 
you want to make a loop that only cycles 5 times then do this:

```
for x in range(0,5):
  print(x)
```

![](https://imgur.com/3xHLLxY.jpg)

You might be asking yourself why this is useful but if you have a list that is **strictly** 5 elements you don't want
cause an index error by asking for an element that isn't there such as the 6th, 7th, ... element

this is where range functions are the most useful, list indexes

```
b = ['red', 'green', 'blue', 'yellow']
for x in range(0,4):
  print(b[x])
```
![](https://imgur.com/X1pvjyc.jpg)

why does this work? because:
```
range(0,4)==[0,1,2,3]

b[0]=='red'
b[1]=='green'
b[2]=='blue'
b[3]=='yellow'
```

![](https://imgur.com/dyFep7h.jpg)

## Nested for loop:

a nested for loop is simpler than it seems, sometimes you have a list where every element is a list itself. 
for example: 

`a = [[8,2,3], [6,4,7]]`

to go through every elements we can do a loop to go through each list, as you know if we want to get every element we have to get the list it's in, then interate over every element in that list

```
a = [[8,2,3], [6,4,7]]
for l in a: #l is a list
  for e in l: #e is an element of the current list
    print(e)
```

![](https://imgur.com/OamF8a9.jpg)

if we want to refer to what row we're in, which you will have to when doing these problems.
The current list here is represented by `l` which you can access in your nested loop

```
a = [[8,2,3], [6,4,7]]
for l in a: 
  for e in l: 
    print('list: ', l, 'element:', e) 
```

![](https://imgur.com/Bf16gEu.jpg)

##### [do this problem](https://www.hackerrank.com/challenges/python-loops)


# List Comprehensions ✌️🏖

You thought for loops were dope, wait till you hear about list comprehensions.

I'm gonna make this one very simple, this is all you'll need to know about them so write it down

list comprehesion lets us make a list of elements that we've performed some operation on, from another list, this can be anything

say we need to make a list of all [2,3,6,4] mulitplied by 2, desired output is [4,6,12,8]

Go ahead try it out... 

commonly the answer would be:

```
given_list = [2,3,6,4]
result = []
for x in given_list:
  result.append(x*2)
print(result)
```
![](https://imgur.com/jqT8qNs.jpg)

very good!

now what if we could make this process infinitely easier and in one line

this is the only thing you need right here and are gonna need out of List Comprehensions

```
given_list = [2,3,6,4]
result = [x*2 for x in given_list]
print(result)
```
![](https://imgur.com/dVmDORD.jpg)

the most important thing you take away from this is 

`[x*2 for x in given_list]`

you can do any operation here believe it or not, heres a few:

###### Numbers 🔢
for lists made up of numbers

`[x**2 for x in given_list] #x squared` 

`[x+2 for x in given_list] #addition`

`[x-2 for x in given_list] #substraction`

###### Strings 🧵
for lists made up of strings

`[s.higher() for s in given_list] #uppercase s (string)`

`[s.lower() for s in given_list] #lowercase s`

the point is you can do **literally** any operation in python on every element from a list and store it in a new one, 
they will definitely ask you about this so remember that format

#### Video:
[![watch](https://img.youtube.com/vi/AhSvKGTh28Q/0.jpg)](https://www.youtube.com/watch?v=AhSvKGTh28Q)

[next page](https://github.com/officialnico/py-tutorial/blob/main/open_sesame.md)



