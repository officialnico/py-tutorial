#Opens the csv file and stores the text
file = open('numbers.csv','r') 
text = file.read()
file.close()

#Strips away the sorrounding spaces
text = text.strip()

#Splits the text into it's corresponding rows
rows = text.split("\n")

#after that: rows == [['22,36,82,20'],['89,21,23,134']]
#Splits rows by their commas and stores them back in the same place

for i in range(0,len(rows)):
  rows[i]=rows[i].split(',')
    
#after that: rows == [['22', '36', '82', '20'], ['89', '21', '23', '134']]

##let's convert the strings to floats

for row in rows:
  for element in row:
    current_row_i = rows.index(row)
    current_element_i = row.index(element)
    rows[current_row_i][current_element_i] = float(element)


big_list = []

for row in rows: 
  for element in row:
    small_list = [] #small list resets every time
    if(element<65): #grading limit
      small_list.append(row.index(element)) #list.index(element) will return the index of that element
    big_list.append(small_list) #now you append small_list to big_list which unlike small_list, doesn't reset
    
#after that: big_list == [[0,1,3],[1,2]]

#Now print the elements inside big_list (in this case the 2 lists)

for l in big_list:
  print(l)
  
  
