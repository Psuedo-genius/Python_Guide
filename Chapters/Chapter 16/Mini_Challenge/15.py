# What will `reversed("abc")` return?
a = "abc"
print(reversed(a))
# <reversed object at 0x0000024A66CC55A0>
# nstead use like this
print(list(reversed(a)))
