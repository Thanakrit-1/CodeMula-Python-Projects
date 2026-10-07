print("Welcome to Student Score Manager")

# สร้าง List 2 ตัวเพื่อเก็บชื่อและคะแนนแยกกัน
students = []
scores = []

while True:
    # แสดงเมนูหลัก
    print("\n1. Add a student score")
    print("2. Remove a student")
    print("3. Show all scores and grades")
    print("Type 'exit' to quit")

    menu = input("Your choice: ")

    # เมนู 1 รับทั้งชื่อและคะแนน รวมถึงเช็กความถูกต้อง
    if menu == "1":
        name = input("Enter student name: ")
        score = input("Enter score: ")

        # ตรวจสอบชื่อต้องเป็นตัวอักษร และ คะแนนต้องเป็นตัวเลข
        if name.isalpha():
            if score.isdigit():
                students.append(name.title())
                scores.append(score)
                print(f"Add {name.title()} with score {score} successfully")
            else:
                print("Error Score a number only!")
        else:
            print("Error Name letters only!")

    # เมนู 2 พิมพ์ชื่อนักเรียนเพื่อลบข้อมูลออก
    elif menu == "2":
        if len(students) == 0:
            print("List is empty")
        else:
            remove_name = input("Enter student name to remove: ").title()

            if remove_name in students:
                index = students.index(remove_name)
                students.pop(index)
                removed_score = scores.pop(index)
                print(f"Removed {remove_name} Score: {removed_score} successfully")
            else:
                print(f"Student '{remove_name}' not found!")

    # เมนู 3 แสดงชื่อ คะแนน และเกรด
    elif menu == "3":
        if len(scores) == 0:
            print("List is empty")
        else:
            for i in range(len(students)):
                score = int(scores[i])

                if score >= 80:
                    grade = "A"
                elif score >= 70:
                    grade = "B"
                elif score >= 60:
                    grade = "C"
                elif score >= 50:
                    grade = "D"
                else:
                    grade = "F"

                print(f"{i+1}. {students[i]} -> Score: {score}, Grade: {grade}")

    # เมนู exit เพื่อออกจากโปรแกรม
    elif menu == "exit":
        break

    # ถ้าพิมพ์ตัวเลือกไม่ถูกต้อง
    else:
        print("Invalid choice!")

print("Goodbye")