# Create a reusable greeting function with default + keyword usage.
def fun(name="User"):
    print("Hello", name)


fun()                 # ➝ uses default: "User"
fun(name="mario")     # ➝ keyword argument
fun("mario")          # ➝ positional argument
