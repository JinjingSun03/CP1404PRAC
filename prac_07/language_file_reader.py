class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        return f"{self.name} (Typing: {self.typing}, Reflection: {self.reflection}, Year: {self.year}, Pointer Arithmetic: {self.pointer_arithmetic})"

def main():
    languages = []
    with open('languages.csv', 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)
