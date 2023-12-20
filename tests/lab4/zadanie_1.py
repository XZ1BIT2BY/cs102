class Movie:
    def __init__(self, movie_id, title):
        # Инициализация объекта фильма с идентификатором и названием
        self.movie_id = movie_id
        self.title = title


class RecommendationSystem:
    def __init__(self, movies_file, views_file):
        # Инициализация системы рекомендаций с данными о фильмах и истории просмотров
        self.movies = self.load_movies(movies_file)
        self.views_history = self.load_views_history(views_file)

    def load_movies(self, file_path):
        # Загрузка данных о фильмах из файла
        movies = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Разделение строки на части по запятой
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    # Извлечение идентификатора и названия фильма
                    movie_id, title = int(parts[0]), ','.join(parts[1:])
                    # Создание объекта Movie и добавление в словарь
                    movies[movie_id] = Movie(movie_id, title)
        return movies

    def load_views_history(self, file_path):
        # Загрузка истории просмотров пользователей из файла
        views_history = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue
                # Преобразование строки в список целых чисел
                views = list(map(int, line.strip().split(',')))
                # Добавление списка просмотров в общий список истории
                views_history.append(views)
        return views_history

    def recommend_movie(self, user_views):
        # Шаг 1: Находим всех пользователей с общими фильмами (включая пользователя)
        all_users = [views for views in self.views_history if set(user_views) & set(views)]

        # Шаг 2: Исключаем фильмы, которые пользователь уже посмотрел
        already_watched = set(user_views)
        eligible_movies = [movie_id for views in all_users for movie_id in views if movie_id not in already_watched]

        # Шаг 3: Выбираем фильм с максимальным числом просмотров
        if eligible_movies:
            recommended_movie_id = max(set(eligible_movies), key=eligible_movies.count)
            recommended_movie = self.movies.get(recommended_movie_id)
            print(f"Рекомендация: {recommended_movie.title} (ID: {recommended_movie.movie_id})")
            return recommended_movie.title
        else:
            print("Нет рекомендаций")
            return "No recommendations"


if __name__ == "__main__":
    # Задаем пути к файлам с данными о фильмах и истории просмотров пользователей
    MOVIES_FILE = "movies.txt"
    VIEWS_FILE = "views_history.txt"

    # Создаем экземпляр RecommendationSystem
    recommendation_system = RecommendationSystem(MOVIES_FILE, VIEWS_FILE)

    # Получаем список просмотров текущего пользователя через пользовательский ввод
    user_views_input = input("Введите список просмотров пользователя через запятую: ")
    user_views = list(map(int, user_views_input.split(',')))

    # Получаем рекомендацию и выводим результат
    recommendation = recommendation_system.recommend_movie(user_views)
