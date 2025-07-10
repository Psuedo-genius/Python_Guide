# What will this print?
for i in range(2):
    for j in range(2):
        print(i, j)
'''
Output:
0 0
0 1
1 0
1 1'''
# Explanation:
'''In this code, we first initialize two nested loops, one for 'i' and
the other for 'j'. The outer loop runs twice (i.e., range(2)), and the inner
loop runs twice as well. Inside each nested loop, we print the values
of 'i' and 'j'. The output shows that the nested loops correctly print the
values of 'i' and 'j' in the range of 0 to 1, inclusive. The outer loop runs
twice, and the inner loop runs twice for each iteration of the outer loop.'''
# its like first print the i loop starts which is zero and then j loop starts
# and complete itself and then i loop starts again and j loop starts again.
# Hope this was understood!
