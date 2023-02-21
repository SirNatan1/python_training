# In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops.
# Python provides 2 loops: 1) for  2) while

# A while loop is used to repeat a block of code as long as a certain condition is true. The condition is checked at the 
# beginning of each iteration, and if it is true, the loop body is executed. The loop continues until the condition becomes false.
#examples: 
count = 0
while count < 5:
    count = count + 1 
    #once the condition is met the function will stop

# insted of ending the code we can continue it by using the else condition after the while, in this case instead of ending the code
# we print the value of the variable which is 5 thats why it ends the loop
# else:
#     print(count)

# using a break
# it's possible to stop the loop by using 'break' inside the loop
a = 0
while a < 5:
    print(a)
    a = a + 1
    if a == 3:
        break
# in this case the code will run the same but since we add a condition if the var = 3 the function will stop

# using continue
# With the continue statement we can skip the current iteration, and continue with the next:
b = 0
while b < 5:
    b = b + 1
    if b == 3:
        continue
    print(b)
# here we can see that once the function was equal to 3 it skipped and moved on, we can tell by seeing the result without the number 3