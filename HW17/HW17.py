class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}

    def _add_grades(self, subj, mark):
        self.grades.setdefault(subj, [mark])
        return self.grades

    def add_mark(self, subj, mark):
        try:
            mark = int(mark)
        except ValueError:
            print("Wrong value")
            return self.grades
        if self.grades.get(subj) is None:
            return self._add_grades(subj, mark)
        mark_list = self.grades[subj]
        mark_list.append(int(mark))
        return self.grades

    def check_grades(self):
        text = ""
        for string_var in self.grades:
            text += f"{string_var}\t :\
 avr({round(sum(self.grades[string_var]) / len(self.grades[string_var]), 2)})\
\tMarks:{self.grades[string_var]}\n"
        result = f"Student:{self.name}\n{'=' * 13}\n{text}"
        return result


class Group:
    def __init__(self, name):
        self.name = name
        self.st_list = set()

    def group_upd(self, obj):
        self.st_list.add(obj)
        return self.st_list

    def show_st(self):
        st_list = list(self.st_list)
        print(f"\nGroup name: {self.name}\n{'-' * 17}")
        print("List of students:\n")
        for index, st in enumerate(st_list):
            print(f"{index + 1}) {st.name}\tage:{st.age}")

    def show_grades(self):
        st_list = list(self.st_list)
        print(f"\nGroup name: {self.name}\n{'-' * 17}")
        print("List of students:\n")
        for index, st in enumerate(st_list):
            print(f"{st.check_grades()}")

st_1 = Student("Thierry", 21)
st_2 = Student("Henry", 18)

st_1.add_mark("Math", 91)
st_1.add_mark("Math", 78)
st_1.add_mark("Math", 77)
st_1.add_mark("Physics", 88)
st_2.add_mark("Math", 99)

group = Group("INTRO")
group.group_upd(st_1)
group.group_upd(st_2)

print("Menu:")
while True:
    print("Select group:")
    print(f"1) {group.name}")
    try:
        selected_group = int(input("Input: "))
    except ValueError:
        break

    selected_group = group   # Just 1 var
    while True:
        print("\nSelect variant:")
        print("1) Show list of students")
        print("2) Check grades")
        try:
            select_var = int(input("Input: "))
        except ValueError:
            break
        if select_var == 1:
            selected_group.show_st()
        if select_var == 2:
            selected_group.show_grades()