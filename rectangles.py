__author__ = 'january'

rectangles = [[0, 1, 3, 3], [2, 2, 6, 4], [1, 0, 3, 5]]
total = 0
intersections = []
for i, rectangle in enumerate(rectangles):
    area = (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])
    total += area

for i, rectangle in enumerate(rectangles):
    remain = rectangles[i + 1:]
    for j, compare in enumerate(remain):
        intersection = [max(rectangle[0], compare[0]), max(rectangle[1], compare[1]), min(rectangle[2], compare[2]),
                        min(rectangle[3], compare[3])]
        intersection_area = (intersection[2] - intersection[0]) * (intersection[3] - intersection[1])
        intersections += [intersection]
        total -= intersection_area

print(intersections)
print(total)