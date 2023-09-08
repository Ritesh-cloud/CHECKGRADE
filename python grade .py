#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check_success(grade):
    if grade >= 60:
        return True
    else:
        return False

def display_message(success):
    if success:
        print("Congratulations! You have succeeded.")
    else:
        print("Unfortunately, you did not succeed this time.")

# Prompt the user for their grade
grade = int(input("Enter your grade: "))

# Check if the grade represents success
success = check_success(grade)

# Display the appropriate message
display_message(success)


# In[ ]:




