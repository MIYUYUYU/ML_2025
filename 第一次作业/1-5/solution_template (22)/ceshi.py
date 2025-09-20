class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = None):
        self._balance = total_sum
        self._balance_limit = balance_limit
    @property
    def balance(self):
        if self._balance_limit == 0:
            raise ValueError("Balance check limits exceeded.")
        else:
            return self._balance

    @property
    def balance_limit(self):
        if self._balance_limit == 0:
            raise ValueError("Balance check limits exceeded.")
        else:
            return self._balance_limit

    def __add__(self, other):
        new_balance = self.balance + other.balance
        if self.balance_limit is None or other.balance_limit is None:
            new_balance_limit = None
        else:
            new_balance_limit = max(self.balance_limit, other.balance_limit)
        return BankCard(new_balance, new_balance_limit)

    def __call__(self, amount: int):
        if self._balance - amount < 0:
            raise ValueError(f"Not enough money to spend {amount} dollars")
        else:
            self._balance -= amount
            print(f"You spent {amount} dollars.")

    def __str__(self):
        return "To learn the balance call balance."

    def put(self, amount: int):
        self._balance += amount
        print(f"You put {amount} dollars.")

a = BankCard(10)
print(a.total_sum)
print(a.balance_limit)
try:
    a(20)
except ValueError as e:
    print(e)
print(a)
a.put(3)
print(a.balance)
b = BankCard(10)

print((a + b).balance)
#var = MyClass().f()
#print(var)