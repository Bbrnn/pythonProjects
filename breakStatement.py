"""
A break statement is used to break or stop a flow control. 
This is generally used in a loop. 
A break statement is used in a loop in such a way, that when a particular condition becomes true, the break statement is executed and we come out of the loop immediately at that moment. 
"""
my_list=[x for x in range(11)]
for i in my_list:
    if i==7:
        break
    print(i)
# What is the output of this code?
else:
    print("logical python")