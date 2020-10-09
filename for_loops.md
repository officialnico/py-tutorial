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

the range functions is how most people first learn to use for loops
the functions is simple, you say what index you wish to start at, and which one to end at.
This is useful because if you know you want to run your for loop only, lets say, 5 times--then you can.

the range function will bring you the list of numbers from your start to finish

```
r = range(0,5)
print(r)
```
![](https://imgur.com/84xHYVf.jpg)

therefore, in this case `range(0,5)==[0,1,2,3,4]`

You want to make a loop that only cycles 5 times then do this:

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
