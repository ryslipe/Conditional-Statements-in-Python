#!/usr/bin/env python
# coding: utf-8

# # Conditional Statements in Python

# ## Five Logical Operators

#     Logical operators are important in many programming languages and Python is no different. We use logical operators when comparing objects and making if statements, for loops, and while loops. When working with data we can use logical operators to implement a block of code given a condition being true or false, or receive a boolean value for a logic that we have passed. For example, we can type 4 > 5 which asks Python if 4 is greater than 5. Since this is false, Python will return 'False'. We may need to use this greater than logical operator in practice when we are applying a bonus to an employee for selling a certain amount of items. If the number they sold is greater than the amount to receive a bonus, Python will run the code for the condition that it is true. We will discuss if statements later, but the logical operator is an important part of that functionality. We may also run a specific code for strings as well. We can use == which tells us if a number or string is equal to another. This is different than the single = symbol because we are not assigning a value in this scenario we are simply checking for identical values/strings. This can be the case if we are working with a website that responds to user input. If a customer inputs that they need their car door replaced they may be prompted with a question asking if it is the left or right door. From there we can use an if statement that will check for the string to match a string we are looking for and run code based on the response. Here we would ask Python if user_input == "Left" then order a left car side door, or something along those lines. 

# | The Command | The Description | Example | Result
# | --- | --- | --- | --- | 
# | > | Greater Than | 4 > 5 | False |
# | == | Is Equal To | "Run" == "Run" | True | 
# | <= | Less Than or Equal To | 12 <= 20 | True
# | and | And | 2 < 3 and 3 < 4 | True 
# | != | Not Equal To | "Was" != "Twas" | True
# 

# In[3]:


4 > 5


# In[4]:


"Run" == "Run"


# In[5]:


12 <= 20


# In[6]:


2 < 3 and 3 < 4


# In[7]:


"Was" != "Twas"


# ## Selection Operators

#     As we saw in the last section, if statements are an important tool to run code based on a certain condition. These codes often work hand-in-hand with logical operators to specify that condition. An if statement takes a condition and will execute code based on the result of the given condition. A simple example can be used with logical operators to execute code based on the result. Let's say we set up a condition for gas mileage where we will get gas if the miles to empty count is less than 50 miles. The logical operator in this case would be the < symbol. In Python, we can create a variable for the gas that we have left in our car such as gas_mileage and set it equal to our current mileage. For example, gas_mileage = 40. With the information we now have we can use a selection operator called an if statement to determine if we need to get gas. In this example the gas mileage is indeed less than 50 miles so we would execute the code listed for when this condition is met. This type of operator is used often in data science and statistics because we will often need to execute code based on certain numbers. If we are working in a marketing firm we may want to cancel a product or service if the satisfaction rating is less than a certain amount. We may also be running analysis of user input on surveys and forms that require us to act on different answers in different ways. The if statement can make this process very easy for us. Once we have the conditions and if statements set up we will run code for the possible scenarios that we have listed. 

# In[1]:


gas_mileage = 40
if gas_mileage < 50:
    print("Get gas.")


# ### Another Example

# In[11]:


favorite_team = input("Enter your favorite team: ")
if favorite_team == "Yankees":
    print(favorite_team)
if favorite_team == "Red Sox":
    print("Your favorite team is the Red Sox")
if favorite_team == "Orioles":
    print("Your favorite team is the Orioles")   
if favorite_team == "Rays":
    print("Your favorite team is the Rays")
if favorite_team == "Blue Jays":
    print("Your favorite team is the Blue Jays.")


# Another beneficial aspect of an if statement is an if/else statement. This is mostly used when we have two possibilities such as flipping a coin. We set up a condition for when an occurence is true, and if it is, we run execute the code in the body. If that condition is false, we move on to the else portion of the statement and run the code that follows. With our American League East favorite teams example we can set up an else statement that will print code for if the user was to type a team that is not in this division. If the user was to type in a team like the Mets, we would execute the else statement because none of the conditions in the if statement were met. 

# In[10]:


favorite_team = input("Enter your favorite team: ")
if favorite_team == "Yankees":
    print(favorite_team)
if favorite_team == "Red Sox":
    print("Your favorite team is the Red Sox")
if favorite_team == "Orioles":
    print("Your favorite team is the Orioles")   
if favorite_team == "Rays":
    print("Your favorite team is the Rays")
if favorite_team == "Blue Jays":
    print("Your favorite team is the Blue Jays.")
else:
    print("Invalid Entry.")


#    In the previous example we see that we can use an if statement to print strings or also print the variable that the user entered. We can use an if statement to have 5 blocks of code by using a new if statement for each possible outcome. This is a good example of how an if statement works but a better way to program this code would be to use an if/else statement. This statement is very similar to the if/else statements in R but they are called elif statements. These start the same by having a condition that is checked and if true it will run the code block in the body of the if statement. This becomes different than an if statement because if the condition is false we reach our elif statement and run that code block based on a certain condition. We can have as many elif statements in our else/if statement as we want. We can run the same code as the previous example but use an elif statement instead of four if statements which makes our code more readable. Another difference between using an elif statement to run the same code we previously did is that once the condition is true it will run the code block that meets the condition and break out of the code. In the previous example using multiple if statements we can have multiple conditions that will be executed if they are true. For instance, we can insert an if statement that says...

# In[8]:


if favorite_team == "Rays":
    print("You like the Rays")


# Since we used multiple if statements in this case, if favorite_team == "Rays" then we will print two statements because there are two conditions that are met for the variable being equal to "Rays". When we use an elif statement, if we do this same process with two elif favorite_team == "Rays" and the input is indeed equal to "Rays", only the first code block will be executed because once the condition is met the code is executed and the elif statement is completed. 

# In[12]:


favorite_team = input("Enter your favorite team: ")
if favorite_team == "Yankees":
    print(favorite_team)
elif favorite_team == "Red Sox":
    print("Your favorite team is the Red Sox")
elif favorite_team == "Orioles":
    print("Your favorite team is the Orioles") 
elif favorite_team == "Rays":
    print("Your favorite team is the Rays.")
elif favorite_team == "Blue Jays":
    print("Your favorite team is the Blue Jays.")

else:
    print("error")


# ### Switch Statements

# While there is no switch statement in Python like there is in R we can still execute a switch statement if we create a funciton and a dictionary. When we use a switch statement we are basically using an elif statement but making it more readable and we are less likely to commit errors in our code. This can be beneficial to us in data science because often times we have many different conditions and outcomes. When this is the case an elif statement can get long and hard to follow which can make things difficult for us and anyone else who is reading our code. A dictionary can act like a switch statement because a dictionary has a key, a value, and together they are an item. We can have 5 different keys which can be thought of as five different conditions and then use a function to get a certain key which acts as the condition to be returned. In the following example we have our familiar prompt asking a user to enter their favorite team. Once we have their favorite team assigned to the variable favorite_team we call our function that we named team. Our function has a dictionary called switch to resemble a switch function in R. This dictionary has the keys as the team names and the values set to be the print statements. We then set a return statement at the end of the function to return switch.get(favorite_team, 'error'). This print statement is getting the key located at favorite_team within the dictionary. This location will be the spot of wherever the team name matches the input from the user. If there is no match, we return error. As we notice with this code, we are saving 3 lines from the elif statement we previously used. 

# In[30]:


def team(favorite_team):
    switch = {
        'Yankees': 'Your favorite team is the Yankees',
        'Red Sox': 'Your favorite team is the Red Sox',
        'Orioles': 'Your favorite team is the Orioles',
        'Blue Jays': 'Your favorite team is the Blue Jays',
        'Rays': 'Your favorite team is the Rays'
    }
    return switch.get(favorite_team, 'error')
favorite_team = input('Enter the number of your favorite team: ')
team(favorite_team)


# ## Loops

# ### For Loop Incrementing 20 Values

# In[32]:


for num in range(1,21):
    print(num)


# ### Using Python's Next Equivalent

# Python has a next() function that is used to access the next iterator, but using the 'continue' key word is most similar to the next function that we used in R. When we use continue we are telling Python to continue on to the next iteration without executing the code below when a condition is true. If we want to only print odd numbers in a range we can use this continue statement. To access only even numbers we can use % 2 == 0. This tells us if the number has a remainder when being divided by zero. When this condition is true we tell Python to continue on to the next iteration without printing the number. When this is false, Python will finish the current iteration by printing the number, which will be odd. Since we want to include 35 in our print statement we will set the range to 36 because a range will include the first number but not include the last number [x, y). 

# In[37]:


for odd in range(36):
    if odd % 2 == 0:
        continue
    print(odd)


# ## Functions 

# I introduced functions briefly in the last section when I was providing an example of the switch statement. A function is a set of instructions that can take perameters/arguments, or not take any at all. When we "call" our function we execute the code that is listed inside the function. As we saw when we made a function to define a switch statement, we took an argument called favorite_team and then executed the code inside the function. This function consisted of a dictionary and we returned switch.get(favorite_team) along with a default value. This code saved us three lines and made our code easier to read. It also helps us when we are making changes to our code or trying to find errors within our code. We can call this function anytime we need the code inside to be executed. If we have 10 different people responding to our question of their favorite team, we do not have to make elif statements 10 times to do so. We can simply call the code 10 different times which is much easier to read and much less likely for us to make errors with. Finding an error in a function is much easier than finding an error in 10 different elif statements. In data science it is very common to have to make the same computations on many different variables and this is an excellent way to do so. We can portray the use of functions further by applying them to multiplication of scalars, vectors, and matricies. 

# In[63]:


def scale(a, b, c, d, e):
    value = a * b * c * d * e
    return value
a = 1 
b = 2
c = 3
d = 4
e = 5
scale(a, b, c, d, e)


# ### Vector Multiplication Using a Function

# In[71]:


import numpy as np


# In[72]:


import matplotlib.pyplot as plt


# In[79]:


a = np.array([3, 3])
b = np.array([2, 2])


# In[80]:


c = np.array([5, 5])
d = np.array([10, 2])
e = np.array([1, 1])


# In[81]:


def vec_mult(a, b, c, d, e):
    result = a * b * c * d * e
    return result


# In[82]:


vec_mult(a, b, c, d, e)


# The preceeding code shows that we import numpy to create arrays that will allow for vector multiplication. We also import matplotlib so we can graph our results. To create this function we need to execute the multiplication of 5 vectors which we do in the function body. We can then pass in the 5 vectors that we created named a, b, c, d, and e. Once these values are passed in to the function the body of the function is executed and our result of [300, 60] is returned. Coding in this fashion will allow us to make changes to the vectors or make new vectors without having to manually type the multiplication everytime. We can simply call the function with the new vectors and it will do the multiplication for us. 

# In[83]:


### Matrix Multiplication Using a Function


# We can create a function for matrix multiplication in a similar process. The first step is to create five matrices. After we create the matrices we can set up a function that multiplies them together. 

# In[ ]:


a = np.array([])

