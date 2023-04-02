class Tour:

    non_alcoholic_members = 0
    alcohlic_members = 0
    expenses = {}

    def __init__(self, person_name, is_alcoholic):
        self.person_name = person_name
        self.is_alcoholic = is_alcoholic
        if eval(self.is_alcoholic):
            Tour.alcohlic_members += 1
        else:
            Tour.non_alcoholic_members += 1

    def read_expense(self, _date, money, where):
        if not Tour.expenses.get(_date, None):
            Tour.expenses[_date] = {self.person_name: {where: money}}
        else:
            if self.person_name in Tour.expenses[_date].keys():
                if where in Tour.expenses[_date][self.person_name]:
                    Tour.expenses[_date][self.person_name][where] = Tour.expenses[_date][self.person_name][where] + money
                else:
                    Tour.expenses[_date][self.person_name][where] = money
            else:
                Tour.expenses[_date][self.person_name] = {where : money}

        return Tour.expenses

    def spent_amount_by_each_person(self, expenses):
        '''returns a dictionary which has spendings of each individual for non alcohol and alcohol events'''
        spent_amount = []
        spent_amount_alcohol = []
        total_amount_spent_by_person = {}
        for _date in expenses.keys():
            if self.person_name in expenses[_date].keys():
                if 'Alcohol' in expenses[_date][self.person_name].keys():
                    spent_amount_alcohol.append(expenses[_date][self.person_name]['Alcohol'])
                    del expenses[_date][self.person_name]['Alcohol']
                spent_amount.extend(expenses[_date][self.person_name].values())
        spent_amount = sum([int(i) for i in spent_amount])
        spent_amount_alcohol = sum([int(i) for i in spent_amount_alcohol])
        total_amount_spent_by_person['Non_Alcohol'] = spent_amount
        total_amount_spent_by_person['Alcohol'] = spent_amount_alcohol
        return total_amount_spent_by_person

    @staticmethod
    def total_expenditure_non_alcohol(people,spent_money):
        non_alcohol = []
        alcohol = []
        for i in people:
            non_alcohol.append(spent_money[i]['Non_Alcohol'])
            alcohol.append(spent_money[i]['Alcohol'])
        return sum(non_alcohol),sum(alcohol)

    @classmethod
    def total_members(cls):
        return cls.alcohlic_members + cls.non_alcoholic_members

    @staticmethod
    def show_spent_amount_by_each(people, spent_amount):
        for person in people:
            spent_amount[person] = people[person].spent_amount_by_each_person(Tour.expenses)
        print(spent_amount)


    @staticmethod
    def show_to_be_paid_by_each(people, spent_amount, Non_alcohol_amount, Alcohol_amount):
        '''displays the final share of every individual for both non alcohol and alcohol events'''
        for person in people:
            NA_person_share = Non_alcohol_amount / Tour.total_members()
            person_contribution = spent_amount[person]["Non_Alcohol"]
            print(f'{person} Non Alcoholic share: {NA_person_share}')
            print(f'spent amount by {person}:{person_contribution}')
            print(f'To be paid by {person} for non alcohol : {NA_person_share - person_contribution}')
        print('=========================')
        for person in people:
            person_contribution = spent_amount[person]["Alcohol"]
            if eval(people[person].is_alcoholic):
                A_person_share = Alcohol_amount / Tour.alcohlic_members
                print(f'{person} Alcoholic share: {A_person_share}')
                print(f'spent amount by {person}:{person_contribution}')
                print(f'To be paid by {person} for alcohol : {A_person_share - person_contribution}')
            else:
                print(f'{person} Alcoholic share: 0.0 ')
                print(f'spent amount by {person}:{person_contribution}')
                print(f'To be paid by {person} for alcohol : {-1 * person_contribution} ')

    @staticmethod
    def read_input_data(input_file_name):
        '''read details of individual and create an object for the same'''
        with open(input_file_name,'r') as person_info:
            people = {}
            is_header = True
            for person in person_info:
                if is_header:
                    is_header = False
                    continue
                name, is_alcoholic = person.split('\t')
                people[name] = Tour(name, is_alcoholic)
            return people

    @staticmethod
    def read_expense_data(expense_file_name,people):
        '''read the expenses from input file,
        call read_expense method to update expenses dictionary
        '''
        with open(expense_file_name,'r') as info:
            is_header = True
            for expenditure in info:
                if is_header:
                    is_header = False
                    continue
                name,_date,amount,where = expenditure.split('\t')
                people[name].read_expense(_date, amount, where.strip())

if __name__ == "__main__":
    people = Tour.read_input_data('C:/Python_Vignesh/finance_calculator/finance_calculator/main/version_one/people_info.txt')
    Tour.read_expense_data('C:/Python_Vignesh/finance_calculator/finance_calculator/main/version_one/spent_info.txt', people)
    print(Tour.expenses)
    spent_amount = {}
    Tour.show_spent_amount_by_each(people,spent_amount)
    Non_alcohol_amount, Alcohol_amount = Tour.total_expenditure_non_alcohol(people,spent_amount)
    #print(Non_alcohol_amount, Alcohol_amount)
    Tour.show_to_be_paid_by_each(people, spent_amount, Non_alcohol_amount, Alcohol_amount)