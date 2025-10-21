score=[63, 47, 76, 77, 28, 24, 28, 92, 60, 65, 10, 31, 86, 39, 59, 83, 35, 19, 6, 98, 67, 52, 20, 18, 86, 24, 7, 18, 19, 86]
max_score=0
for marks in score:
    if marks>=max_score:
        max_score=marks
print(max_score)

#other method

print(max(score))