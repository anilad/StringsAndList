st= "It's thanksgiving day. It's my birthday too!"
#Find and Replace: print the position of the first instance of the word "day" then create a new string where "day" is replaced with "month"
print st.find('day')
print st.replace("day", "month")

x=[2,54,-2,7,12,98]
#Min and Max: print the min and max values in a list
print min(x)
print max(x)

y= ['hello', 2, 54, -2, 7, 12, 98, "world"]
#First and Last: print the first and last values in a list and then create a new list containing only the first and last values of the original list
print y[0]
print y[len(y)-1]
y2=[]
y2.append(y[0])
y2.append(y[len(y)-1])
print y2

z=[19,2,54,-2,7,12,98,32, 10, -3, 6]
#New List: Sort your list first, then split your list in half. Push the list created from the first half to position 0 of the list created from the second half. Output should be [[-3,-2,2,6,7],10,12,19,32,54,98]

z.sort()
z2= z[5:]
z3=z[0:5]
z2.insert(0,z3)
print z2