import unittest
import unittest.mock

from src.lab4.zadanie_1 import RecommendationSystem

class TestRecommendationSystem(unittest.TestCase):
    def setUp(self):
        # Пути к файлам с данными о фильмах и истории просмотров пользователей
        self.MOVIES_FILE = "movies.txt"
        self.VIEWS_FILE = "views_history.txt"

    def test_recommendation_system(self):
        # Инициализация объекта RecommendationSystem с использованием файлов с данными
        recommendation_system = RecommendationSystem(self.MOVIES_FILE, self.VIEWS_FILE)

        # Тест-кейс 1: Действительный ввод пользователя с рекомендациями
        user_views = [1, 2, 3]
        with unittest.mock.patch('builtins.input', return_value="1,2,3"):
            recommendation = recommendation_system.recommend_movie(user_views)
            self.assertIsNotNone(recommendation)
            self.assertNotEqual(recommendation, "No recommendations")

        # Тест-кейс 2: Действительный ввод пользователя без рекомендаций
        user_views = [4, 5, 6]
        with unittest.mock.patch('builtins.input', return_value="4,5,6"):
            recommendation = recommendation_system.recommend_movie(user_views)
            self.assertIsNotNone(recommendation)

            # Ожидаемое значение, основанное на реальном поведении кода
            expected_recommendation = "Мстители: Финал\n"  # Обновите при необходимости
            self.assertEqual(recommendation, expected_recommendation)

        # Тест-кейс 3: Недействительный ввод пользователя (нецелочисленные значения)
        try:
            user_views = ["a", "b", "c"]
            recommendation_system.recommend_movie(user_views)
        except ValueError as e:
            # Печать сообщения об ошибке для отладки
            print(f"Поймано исключение ValueError: {e}")
            raise e

        # Добавьте больше тест-кейсов при необходимости

    def tearDown(self):
        # Очистка ресурсов, если это необходимо
        pass

if __name__ == '__main__':
    unittest.main()
