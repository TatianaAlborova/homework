import unittest
import tests_21_3

test_suite = unittest.TestSuite()

test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_21_3.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_21_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(test_suite)

