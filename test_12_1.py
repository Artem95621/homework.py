import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk1 = runner.Runner('First')
        for i in range(10):
            walk1.walk()
        self.assertEqual(walk1.distance, 50)

    def test_run(self):
        run1 = runner.Runner('Second')
        for j in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)

    def test_challenge(self):
        challenge1 = runner.Runner('Third')
        challenge2 = runner.Runner('Fourth')
        for k in range(10):
            challenge1.run()
            challenge2.walk()
        self.assertNotEqual(challenge1.distance, challenge2.distance)


if __name__ == '__main__':
    unittest.main()