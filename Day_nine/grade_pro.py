student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermoine":99,
    "Draco":74,
    "Neville":62
}

stud={}

for key in student_scores:
    #print(student_scores[key])
    if 91 <= student_scores[key] <= 100:
        stud[key] = "Outstanding"
    elif 81 <= student_scores[key] < 90:
        stud[key]="Exceeds the expectation"
    elif 71 <= student_scores[key] < 80:
        stud[key]="Acceptable"
    else:
        stud[key]="Fail"
print(stud)