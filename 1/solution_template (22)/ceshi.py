num = int(input())
num1 = num % 10
num //= 10
num_ten = num % 10
num //= 10
num_hundred = num % 10
num_thousand = num // 10
num_di = [num_thousand, num_hundred, num_ten, num1]
num_thousand_map = {
        1 : "M",
        2 : "MM",
        3 : "MMM",
        0 : ""
    }
num_hundred_map = {
        1 : "C",
        2 : "CC",
        3 : "CCC",
        4 : "CD",
        5 : "D",
        6 : "DC",
        7 : "DCC",
        8 : "DCCC",
        9 : "CM",
        0 : ""
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
roman_num=num_thousand_map.get(num_di[0])+num_hundred_map.get(num_di[1])+num_ten_map.get(num_di[2])+num1_map.get(num_di[3])
print (roman_num)
