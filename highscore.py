# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# student_scores_sorted = sorted(student_scores)
# print(f"The highest score in the class is {student_scores_sorted[-1]}")
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(highest_score)