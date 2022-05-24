people_in_jury = int(input())
presentation_name = input()

total_average_grade = 0
counter = 0
while presentation_name != "Finish":
    counter += 1
    current_mean_grade = 0
    for person in range(people_in_jury):
        grade = float(input())
        current_mean_grade += grade
    current_average_grade = current_mean_grade / people_in_jury
    print(f'{presentation_name} - {current_average_grade:.2f}.')
    total_average_grade += current_average_grade
    presentation_name = input()

final_average_grade = total_average_grade / counter
print(f"Student's final assessment is {final_average_grade:.2f}.")
