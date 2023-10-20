#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Prompt the user for the bill amount and tip percentage
bill_amount = float(input("Enter the bill amount: $"))
tip_percentage = float(input("Enter the tip percentage you want to leave (e.g., 15 for 15%): "))

# Calculate the tip and total amount
tip_amount = (bill_amount * tip_percentage) / 100
total_amount = bill_amount + tip_amount

# Display the results
print(f"Bill Amount: ${bill_amount:.2f}")
print(f"Tip Amount ({tip_percentage}%): ${tip_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")


# In[ ]:




