import HumanMoveTest
import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        # Инициализация словаря для хранения результатов
        cls.all_results = {}

    def setUp(self):
        # Создание объектов бегунов
        self.runner1 = HumanMoveTest.Runner("Усэйн", speed=10)
        self.runner2 = HumanMoveTest.Runner("Андрей", speed=9)
        self.runner3 = HumanMoveTest.Runner("Ник", speed=3)


    def test_race_1(self):
        # Забег: Усэйн и Ник
        tournament = HumanMoveTest.Tournament(distance=90)
        tournament.participants.append(self.runner1)  # Усэйн
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_race_1'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == 'Ник')


    def test_race_2(self):
        # Забег: Андрей и Ник
        tournament = HumanMoveTest.Tournament(distance=90)
        tournament.participants.append(self.runner2)  # Андрей
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_race_2'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == "Ник")


    def test_race_3(self):
        # Забег: Усэйн, Андрей и Ник
        tournament = HumanMoveTest.Tournament(distance=90)
        tournament.participants.append(self.runner1)  # Усэйн
        tournament.participants.append(self.runner2)  # Андрей
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_race_3'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == "Ник")

    @classmethod
    def tearDownClass(cls):
        # Вывод результатов в столбец
        print("Результаты всех тестов:")
        for k, v in cls.all_results.items():
            formatted_results = {place: str(runner) for place, runner in v.items()}
            print(f"{formatted_results}")


if __name__ == '__main__':
    unittest.main()
