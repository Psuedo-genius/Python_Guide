# Sort dictionary values in descending order.
marks = {99: 'Maths', 78: 'English', 79: 'Physics', 67: 'Chemisty'}
# Sort by values (descending) and build a new ordered dictionary
sorted_marks = dict(sorted(marks.items(), key=lambda item: item[1],
                           reverse=True))

print(sorted_marks)
# this all are hard stuff try to understand you will be more clear after
# the function chapter.
