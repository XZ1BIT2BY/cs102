# Определяем класс Respondent (Респондент)
class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age})"


# Определяем класс AgeGroup (Возрастная Группа)
class AgeGroup:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.respondents = []  # Список респондентов в данной возрастной группе

    def __repr__(self):
        return f"{self.lower_bound}-{self.upper_bound}: {', '.join(map(str, self.respondents))}"


# Определяем класс SurveyProcessor (Обработчик Опроса)
class SurveyProcessor:
    def __init__(self, age_groups):
        self.age_groups = age_groups  # Список возрастных групп

    def process_survey(self, respondents):
        # Добавляем каждого респондента в соответствующую возрастную группу
        for respondent in respondents:
            self.add_respondent(respondent)

        # Сортируем респондентов в каждой возрастной группе по возрасту и имени
        for age_group in self.age_groups:
            age_group.respondents.sort(key=lambda x: (x.age, x.name))

        # Фильтруем и выводим непустые возрастные группы в обратном порядке
        for age_group in reversed(self.age_groups):
            if age_group.respondents:
                print(age_group)

    def add_respondent(self, respondent):
        # Добавляем респондента в соответствующую возрастную группу
        for age_group in self.age_groups:
            if age_group.lower_bound <= respondent.age <= age_group.upper_bound:
                age_group.respondents.append(respondent)
                break


def main():
    age_boundaries = [18, 25, 35, 45, 60, 80, 100]
    
    # Создаем объекты возрастных групп на основе границ
    age_groups = [AgeGroup(age_boundaries[i] + 1, age_boundaries[i + 1]) for i in range(len(age_boundaries) - 1)]
    # Добавляем последнюю группу, предполагая, что никто не старше 123 лет
    age_groups.append(AgeGroup(age_boundaries[-1] + 1, 123))

    respondents = []
    
    # Вводим данные респондентов из консоли
    while True:
        input_str = input("Введите данные респондента (или 'END' для завершения): ")
        if input_str == 'END':
            break
        name, age = input_str.split(',')
        # Создаем объект респондента и добавляем его в список
        respondents.append(Respondent(name.strip(), int(age)))

    # Создаем объект SurveyProcessor и обрабатываем опрос
    survey_processor = SurveyProcessor(age_groups)
    survey_processor.process_survey(respondents)


# Запускаем программу при выполнении файла
if __name__ == "__main__":
    main()
