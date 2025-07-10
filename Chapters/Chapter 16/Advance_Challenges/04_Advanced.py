# Create a calculator with `eval()` (warn about risks).
while True:
    expr = input("Enter expression (e.g. 2+3*4), or 'q' to quit: ")
    if expr.lower() == 'q':
        break
    try:
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

'''
⚠️ BIG WARNING: Security Risk
Using eval() with user input can be dangerous.

For example:
eval("__import__('os').system('rm -rf /')")
This can delete files or run malicious code if input is not controlled.
'''
