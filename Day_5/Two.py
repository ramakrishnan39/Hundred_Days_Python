# Find maximum number in the given list with for loops.

# 78 65 89 86 55 91 64 89

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
max_val=0
for score in student_scores:
    if score > max_val:
        max_val=score
print(max_val)
#With the usage of function max()
print(max(student_scores))