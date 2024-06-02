from tkinter import * 
from tkinter import ttk
import sqlite3

class UI:
    def __init__(self,model):
        self.model = model
        self.root = Tk()                 # Creates the Tk main window object
        self.root.geometry("300x450")    # sets the size
        self.frame = Frame(self.root)         # Creates a Frame that allows multiple object to be added
        self.frame.pack()                # Fit the frame in the root
        
        self.label = Label(self.frame, text = "Enter your name:")
        self.label.pack()
        self.text_box1 = Text(self.frame, height = 1, width = 10)
        self.text_box1.pack()

        self.label2 = Label(self.frame, text = "Select Class")
        self.label2.pack()

        self.class_list = ttk.Combobox(self.frame, values = model.get_classes())
        self.class_list.pack()
        self.button = Button(self.frame, text = "Register", command = self.reg_class)
        self.button.pack()

    # Run the main loop
    def run(self):
        self.root.mainloop()

    # Event handler for registering for a class
    # We don't do anything here just send a message to the model to do the work
    def reg_class(self): 
        name = self.text_box1.get(1.0, END)  # gets the text from first text box
        cl = self.class_list.get()           # gets the selected class
        school.add_enrollment(name, cl)       # adds the enrollment to the model
        

class Student:
    def __init__(self, name, id_num,dbid):
        self.name = name
        self.id_num = id_num
        self.dbid = dbid

    def __str__(self):
        return self.name + "(" + str(self.id_num) + ")"
    


class   SchoolClass:
    def __init__(self, name, dbid):
        self.name = name
        self.dbid = dbid
    def __str__(self):
        return self.name
    
class School:
    def __init__(self, db):
        self.db = db
        self.students = []
        self.classes = []
        self.enrollments = []
        db.build_model(self)

    def add_student(self, name, id_num, dbid):
        stu = Student(name, id_num, dbid)
        self.students.append(stu)
        return stu
        
    def add_class(self, name, dbid):
        cl = SchoolClass(name, dbid)
        self.classes.append(cl)
        return cl

    def enroll(self, student_id, class_id):
        stu = [s for s in self.students if s.dbid == student_id]
        cl = [c for c in self.classes if c.dbid == class_id]
        self.enrollments.append((stu, cl))
        print("Enrolled ", str(stu), str(cl))

    # enroll a student in a class
    # first check the student and class exist
    def add_enrollment(self, student_name, class_name):
        stu_a = [s for s in self.students if s.name == student_name.strip()]
        cl_a = [c for c in self.classes if c.name == class_name.strip()]
        if len(stu_a) == 0:
            print("Student not found [", student_name, "]")
            return
        if len(cl_a) == 0:
            print("Class not found")
            return
        stu = stu_a[0]
        cl = cl_a[0]
        self.enrollments.append((stu, cl))
        db.add_enrollment(stu.dbid,cl.dbid)
        print("Enrolled ", stu, cl)

    def get_classes(self):
        return self.classes
    
    def get_students(self):
        return self.students
    
    def get_enrollment(self, student):
        return [cl for cl in self.classes if (student, cl) in self.enrollments]
    
class Database:
    def __init__(self):
        self.con = sqlite3.connect("register.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students (S_ID INTEGER PRIMARY KEY ASC, name TEXT, id_num INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS classes (C_ID INTEGER PRIMARY KEY ASC, name TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS enrollments (S_ID INTEGER, C_ID INTEGER)") 
        self.con.commit()

    def add_student(self, name, id_num):
        self.cur.execute("INSERT INTO students VALUES (NULL, ?, ?)", (name,id_num,))
        self.con.commit()

    def find_student(self, name):
        for stu in self.cur.execute("SELECT * FROM students WHERE name = ?", (name,)):
            return stu.get("S_ID")
        return None
    

    def add_class(self, name):
        self.cur.execute("INSERT INTO classes VALUES (NULL, ?)", (name,))
        self.con.commit()
    
    def add_enrollment(self, student, cl):
        self.cur.execute("INSERT INTO enrollments VALUES (?, ?)", (student, cl))
        self.con.commit()

    def dump(self):
        print("DB Students:"  )
        for stu in self.cur.execute("SELECT * FROM students"):
            print(stu)
        print("DB Classes:"  )  
        for cl in self.cur.execute("SELECT * FROM classes"):
            print(cl)
        print("DB Enrollments:"  )
        for en in self.cur.execute("SELECT * FROM enrollments"):
            print(en)

    # code to build the model here as backend datebase might change 
    def build_model(self, model):
        for stu in self.cur.execute("SELECT * FROM students"):
            model.add_student(stu[1], stu[2], stu[0])
        for cl in self.cur.execute("SELECT * FROM classes"):
            model.add_class(cl[1], cl[0])
        for en in self.cur.execute("SELECT * FROM enrollments"):
            model.enroll(en[0], en[1])
        return model
        
    # fill database with sample data, not for production
    def setUp(self):
        self.cur = self.con.cursor()
        self.cur.execute("DELETE FROM students")
        self.cur.execute("DELETE FROM classes")
        self.cur.execute("DELETE FROM enrollments")
        self.con.commit()

        self.add_student("John Doe",1234)
        self.add_student("Jane Doe",5678)
        self.add_student("Alice", 9876)
        self.add_student("Bob", 5432)
        self.add_class("Math")
        self.add_class("English")
        self.add_class("Science")

db = Database()
db.setUp()
db.dump()
school = School(db)
print("Students:"  )
for stu in school.get_students():
    print(stu)
print("Classes:"  )
for cl in school.get_classes():
    print(cl)
ui = UI(school)
ui.run()
db.dump()
for en in school.enrollments:
    print(en[0], en[1])