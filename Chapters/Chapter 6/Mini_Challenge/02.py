# What happens if all  if  and  elif  are false?
'''Answer: If all if and elif conditions are false,
the code will execute the code block following the else statement.
If no else statement is provided, it will simply skip the else block and
execute the code block following the last if or elif condition that was true'''

# Example usage:
if 2 > 3:
    print('Condition 1 is true')
elif 2 > 3:
    print('Condition 2 is true')
elif 3 > 3:
    print('Condition 3 is true')
else:
    print('No conditions are true')
