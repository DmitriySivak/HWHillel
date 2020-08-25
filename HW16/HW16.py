from dataclasses import dataclass

@dataclass
class Value:
    amount: float
    currency: str

class ATM:
    min_limit = 0
    max_limit = 9999
    bank_name = 'Wells Fargo'

    def __init__(self, amount, currency):
        self.account = 10000
        self.initial_amount = self._validate_amount(amount)
        self.initial_currency = self._validate_currency(currency)
        self.curr_map = {'UAH': 1, 'USD': 27.4, 'EUR': 32.4}

    def _validate_amount(self, amount):
        if amount < 0:
            raise ValueError
        return amount

    def _validate_currency(self, currency):
        if currency not in {'USD', 'EUR', 'UAH'}:
            raise ValueError
        return currency

    def add_money(self):
        self.account += self.initial_amount * self.curr_map.get(self.initial_currency)
        return round(self.account, 2)

    def withdraw(self):
        if self.account < self.initial_amount:
            raise ValueError('Not enough money to cash out')
        elif self.initial_amount > self.max_limit:
            raise ValueError('Limit is exceeded')
        self.account -= self.initial_amount * self.curr_map.get(self.initial_currency)
        return round(self.account, 2)

action_1 = ATM(20, 'USD')
action_2 = ATM(10, 'EUR')
action_3 = ATM(15, 'UAH')

action_1.add_money()
action_2.withdraw()
action_3.withdraw()

print(action_1.account)
print(action_2.account)
print(action_3.account)