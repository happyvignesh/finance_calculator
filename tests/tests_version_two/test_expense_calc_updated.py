import unittest
from finance_calculator.main.version_two.expense_calc_updated import Tour


class TestTour(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        people, total_expenses, individual_share = Tour.read_expense_data('test_data.txt')
        cls.people = people
        cls.total_expenses = total_expenses
        cls.individual_share = individual_share

    def test_read_expense_data(self):
        test_total_expenses = {'Gopi': 2000.0, 'Vignesh': 1000.0, 'Karthi': 1000.0}
        test_individual_share = {'Gopi': 1833.3333333333333, 'Vignesh': 333.3333333333333, 'Karthi': 1833.3333333333333}
        people, total_expenses, individual_share = self.people, self.total_expenses, self.individual_share
        for person in people.values():
            self.assertIsInstance(person, Tour, 'given person is not instance of Tour')
        self.assertEqual(total_expenses, test_total_expenses)
        self.assertEqual(individual_share, test_individual_share)

    def test_final_share(self):
        test_final_share = ['To be paid by Gopi : -166.66666666666674', 'To be paid by Vignesh : -666.6666666666667',
                            'To be paid by Karthi : 833.3333333333333']
        actual_share = []
        for person in self.people.keys():
            actual_share.append(Tour.final_share(person))
        self.assertEqual(actual_share, test_final_share, 'Wrong Calculation')
