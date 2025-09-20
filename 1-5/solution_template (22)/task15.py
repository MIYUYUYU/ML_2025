from typing import List


def hello(name:str = None) -> str:
        if name is None or name == '':
            return "Hello!"
        else:
            return f"Hello, {name}!"


def int_to_roman(num: int) -> str:
    num1 = num % 10
    num //= 10
    num_ten = num % 10
    num //= 10
    num_hundred = num % 10
    num_thousand = num // 10
    num_di = [num_thousand, num_hundred, num_ten, num1]
    num_thousand_map = {
        1: "M",
        2: "MM",
        3: "MMM",
        0: ""
    }
    num_hundred_map = {
        1: "C",
        2: "CC",
        3: "CCC",
        4: "CD",
        5: "D",
        6: "DC",
        7: "DCC",
        8: "DCCC",
        9: "CM",
        0: ""
    }
    num_ten_map = {
        1: "X",
        2: "XX",
        3: "XXX",
        4: "XL",
        5: "L",
        6: "LX",
        7: "LXX",
        8: "LXXX",
        9: "XC",
        0: ""
    }
    num1_map = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        0: ""
    }
    roman_num = num_thousand_map.get(num_di[0]) + num_hundred_map.get(num_di[1]) + num_ten_map.get(
        num_di[2]) + num1_map.get(num_di[3])
    return roman_num

def longest_common_prefix(strs_input: List[str]) -> str:
    if len(strs_input) == 0:
        return ""                                   #检查是否为空输入

    stripped_strs = strs_input.copy()
    for i in range(len(strs_input)):
        stripped_strs[i] = strs_input[i].lstrip()   #去除左边空格

    if any(len(word) == 0 for word in stripped_strs):       #检查去除后是否有空
        return ""

    min_len = min(len(word) for word in stripped_strs)
    for i in range(min_len):
      #  current_char = stripped_strs[0][i]
        for word in stripped_strs:
            if word[i] != stripped_strs[1][i] or i >= min_len:
                return stripped_strs[0][:i]
    return stripped_strs[0][:min_len]





def primes() -> int:
    yield 2
    yield 3
    k = 1

    def is_primes(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    p = 5
    while True:
        if is_primes(p):
            yield p
        p += 1


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = None):
        self._balance = total_sum
        self._balance_limit = balance_limit
    @property
    def total_sum(self):
        return self._balance

    @property
    def balance(self):
        if self._balance_limit == 0:
            raise ValueError(" Balance check limits exceeded.")
        elif self._balance_limit is not None:
            self._balance_limit -= 1
            return self._balance
        else:
            return self._balance

    @property
    def balance_limit(self):
        if self._balance_limit == 0:
            raise ValueError("Balance check limits exceeded.")
        else:
            return self._balance_limit

    def __add__(self, other):
        new_balance = self._balance + other._balance
        if self._balance_limit is None or other._balance_limit is None:
            new_balance_limit = None
        else:
            new_balance_limit = max(self._balance_limit, other._balance_limit)
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

