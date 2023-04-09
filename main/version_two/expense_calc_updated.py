class Tour:

    expenses = {}
    individual_share = {}

    def __init__(self, person_name):
        self.person_name = person_name

    @classmethod
    def final_share(cls, person_name):
        each_share = cls.individual_share[person_name] - cls.expenses[person_name]
        return f'To be paid by {person_name} : {each_share}'

    @staticmethod
    def read_expense_data(expense_file_name):
        with open(expense_file_name, 'r') as info:
            people = {}
            is_header = True
            for expenditure in info:
                if is_header:
                    _, members = expenditure.strip().split('|')
                    members = members.split(',')
                    for name in members:
                        people[name] = Tour(name)
                    is_header = False
                    next(info)
                    continue
                name, _, amount, _, participants = expenditure.strip().split('|')
                participants = participants.split(',')
                if participants[0] == 'All':
                    participants = members
                for i in participants:
                    actual_amount = float(amount) / len(participants)
                    if people.get(i).individual_share.get(i):
                        people.get(i).individual_share[i] = (float(people.get(i).individual_share[i]) + float(actual_amount))
                    else:
                        people.get(i).individual_share[i] = float(actual_amount)

                if people.get(name).expenses.get(name):
                    people.get(name).expenses[name] = float(people.get(name).expenses[name]) + float(amount)

                else:
                    people.get(name).expenses[name] = float(amount)
            return people, people.get(name).expenses, people.get(name).individual_share


if __name__ == "__main__":
    people, total_expenses, individual_share = Tour.read_expense_data('input_details.txt')
    print(f'Total money spent by each person: {total_expenses}')
    print(f'Each person share: {individual_share}')
    final_share_list = []
    for person in people:
        final_share_list.append(Tour.final_share(person))
    print(final_share_list)
