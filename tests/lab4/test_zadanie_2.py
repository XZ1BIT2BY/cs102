import unittest
from io import StringIO
from unittest.mock import patch
from src.lab4.zadanie_2 import Respondent, AgeGroup, SurveyProcessor, main

class TestSurveyProcessor(unittest.TestCase):
    def setUp(self):
        self.age_boundaries = [18, 25, 35, 45, 60, 80, 100]
        self.age_groups = [AgeGroup(self.age_boundaries[i] + 1, self.age_boundaries[i + 1]) for i in range(len(self.age_boundaries) - 1)]
        self.age_groups.append(AgeGroup(self.age_boundaries[-1] + 1, 123))

    def test_process_survey(self):
        respondents = [
            Respondent("Alice", 22),
            Respondent("Bob", 35),
            Respondent("Charlie", 45),
            Respondent("David", 60),
        ]

        survey_processor = SurveyProcessor(self.age_groups)

        with patch('builtins.input', side_effect=['Alice,22', 'Bob,35', 'Charlie,45', 'David,60', 'END']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                survey_processor.process_survey(respondents)

        expected_output = "46-60: David (60)\n" \
                          "36-45: Charlie (45)\n" \
                          "26-35: Bob (35)\n" \
                          "19-25: Alice (22)\n"

        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
