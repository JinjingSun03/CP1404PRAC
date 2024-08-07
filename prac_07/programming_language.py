class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}"

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.typing} Typing"

    def is_dynamic(self):
        return self.typing == "Dynamic"


def run_tests():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, True)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, True)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    cplusplus = ProgrammingLanguage("C++", "Static", True, 1983, True)

    languages = [ruby, python, visual_basic, cplusplus]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
