import copy



spam=[1, 2, 3, 4, 5, 6,7]
cheese= copy.copy(spam)
cheese[3]=8
print(spam)
print(cheese)
