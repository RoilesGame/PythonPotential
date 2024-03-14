# task 1
import csv

with open("students.csv", encoding="utf-8") as csv_file:
    information = list(csv.reader(csv_file))[1:]

    count_class = {}
    sum_class = {}

    for id, name, project_id, level, score in information:
        if "Хадаров Владимир" in name:
            print(f"Ты получил: {score}, за проект - {project_id}")

        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + int(0 if score == 'None' else int(score))

    for row in information:
        if row[-1] == 'None':
            required_class = row[-2]
            row[-1] = round(sum_class[required_class] / count_class[required_class], 3)

with open("student_new.csv", "w", encoding="utf-8") as csv_answer:
    print("id,Name,titleProject_id,class,score", file=csv_answer)

    for id, name, project_id, level, score in information:
        print(f"{id},{name},{project_id},{level},{score}", file=csv_answer)
