# Print triangle pattern of `#` symbols
"""
  #
 ###
#####
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    print(" " * ((n-i)), end="")
    print("#" * (2*i-1))

"""n = int(input("Enter the number of rows: "))

    👦 This asks the user how many rows of pyramid they want.

    For example, if you type 4, you want 4 lines in your pyramid.

for i in range(1, n+1):

    This is a loop — it runs again and again for each row.

    i means: which row are we on now?

    It starts at 1 (the first row) and goes up to n.

Now this line is very important:

print(" " * ((n-i)), end="")

    This prints spaces to move the # to the center like a triangle.

    Let's say n = 4 and i = 1:

        n - i = 3, so we print 3 spaces before the #

    This makes the pyramid go up, not just lean left.

💡 Remember:

    More spaces at the top,

    Fewer spaces at the bottom.

print("#" * (2*i - 1))

    This prints the actual # characters in the row.

    Formula: 2*i - 1

    Why this formula?

        Because each row adds 2 more # than the one above.

        First row: 1 # → 2*1 - 1 = 1

        Second row: 3 # → 2*2 - 1 = 3

        Third row: 5 # → 2*3 - 1 = 5
"""
