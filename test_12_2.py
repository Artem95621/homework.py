import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for key, value in cls.all_result.items():
            for k, v in value.items():
                result[k] = str(v)
            print(result)

    def test1(self):
        first_rase = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        res = first_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res

    def test2(self):
        second_rase = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        res = second_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res

    def test3(self):
        third_rase = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        res = third_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res


if __name__ == '__main__':
    unittest.main()