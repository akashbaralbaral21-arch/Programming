student_mark={"ram":93,"shyam":98,"hari":88, "gita":90}
result=student_mark.get("ram","student not found")
print(result)


student_mark={"ram":93,"shyam":98,"hari":88, "gita":90}

for i in student_mark:
    print(i)
for i in student_mark.keys():
    print(i)
for i in student_mark.values():
    print(i)
for i in student_mark.items():
    print(i)

for i,j in student_mark.items():
    print(i,"    ",j)
    
    
students={
    "ram":{"math":93,"english":90},
    "shyam":{"math":98,"english":95},
    "hari":{"math":88,"english":85},
    "gita":{"math":90,"english":92}
    
}

quiz_data={
    "qno1":{
        "question":"what python library is used for building Desktop GUI?",
        "option":["NumPY", "Tiknter", "Pandas", 'Flask'],
        'answer':"Tkinter"
    },
    "qno2":{
        "question":"what is the result of 4==7 in Python?",
        "options":["True", "False", "Error", "None"],
        "answer":"False"
    },
    "qno3":{
        "question":"which set method "
    }
    
    