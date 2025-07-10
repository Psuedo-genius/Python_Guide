# Given a tuple of 3D points `((x1, y1, z1), (x2, y2, z2), ...)`,
# print only the z-values from each point
points = ((1, 2, 3), (4, 5, 6), (7, 8, 9))  # Tuple of 3D points

for point in points:
    z = point[2]  # Access the z-value (3rd item)
    print(z)
