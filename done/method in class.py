class employee:
    lang="python"
    salary=12000
    dept="AI"

    def info(self):
        print(f"Language is {self.lang}. and salary is {self.salary}")

    def dep(self):
        print(f"Department is {self.dept}.")

harry=employee()
harry.info()
harry.dep()