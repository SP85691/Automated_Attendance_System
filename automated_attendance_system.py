import datetime, json

class Attendance_System():
    def __init__(self):
        total_students = int(input("| Enter The Total Number of Students: "))
        students = [input("| Enter The Name of Student: ") for i in range(total_students)]
        
        while True:
            print("\n+-------------------------------------+")
            print("|               MENU                  |")
            print("+-------------------------------------+")
            print("| 1. Take Attendance for the day.     |")
            print("| 2. View Attendance Records.         |")
            print("| 3. Generate a Report of Absentees.  |")
            print("| 4. Exit                             |")
            print("+-------------------------------------+")
            choice = int(input("| Enter Your Choice (1, ... 4): "))
            print("+-------------------------------------+")

            if(choice == 1):
                self.take_attendance(students)
            elif(choice == 2):
                self.view_attendance()
            elif(choice == 3):
                self.generate_report()
            elif(choice == 4):
                break
            else:
                print("Invalid Choice. Try Again.")
                continue

    def take_attendance(self, students):
        date = datetime.date.today().strftime("%Y-%m-%d")
        self.present_student = []
        self.attendance_record = {}

        print("+---------------------------------------------------------+")
        print("|                      TAKE ATTENDANCE                    |")
        print("+---------------------------------------------------------+")
        print("| Date - {:<49}|".format(date))
        print("+---------------------------------------------------------+")
        print("| Write 'P' to Mark Present the Student or 'A' for Absent |")
        print("+---------------------------------------------------------+")
        for student in students:
            present = input(f"| Is {student} Present Today: ")
            if present == "P":
                self.present_student.append(student)
        print("+---------------------------------------------------------+")
        print("| Attendance Marked Successfully.                         |")
        print("+---------------------------------------------------------+")

        self.attendance_record["Date"] = date
        self.attendance_record["Present"] = self.present_student
        self.attendance_record["Absent"] = [student for student in students if student not in self.present_student]
        with open('AttendanceRecord.json', 'w') as fp:
            json.dump(self.attendance_record, fp)

    def view_attendance(self):
        try:
            with open('AttendanceRecord.json', 'r') as fp:
                self.attendance_record = json.load(fp)
        except:
            print("+---------------------------------------------------------+")
            print("| No Attendance Record Found.                             |")
            print("+---------------------------------------------------------+")
            return

        print("+---------------------------------------------------------+")
        print("|                      VIEW ATTENDANCE                    |")
        print("+---------------------------------------------------------+")
        print("| Date - {:<49}|".format(self.attendance_record['Date']))
        print("+---------------------------------------------------------+")
        print("| Present Students:                                       |")
        print("+---------------------------------------------------------+")
        for student in self.attendance_record["Present"]:
            print("| {:<56}|".format(student))
        print("+---------------------------------------------------------+")

    def generate_report(self):
        try:
            with open('AttendanceRecord.json', 'r') as fp:
                self.attendance_record = json.load(fp)
        except:
            print("+---------------------------------------------------------+")
            print("| No Attendance Record Found.                             |")
            print("+---------------------------------------------------------+")
            return
        
        print("+---------------------------------------------------------+")
        print("| Absent Students:                                        |")
        print("+---------------------------------------------------------+")
        print("| Date - {:<49}|".format(self.attendance_record['Date']))
        print("+---------------------------------------------------------+")
        for student in self.attendance_record["Absent"]:
            print("| {:<56}|".format(student))
        print("+---------------------------------------------------------+")

if __name__ == "__main__":
    AS = Attendance_System()