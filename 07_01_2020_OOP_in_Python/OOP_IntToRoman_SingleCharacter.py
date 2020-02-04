class Numbers:
    def IntToRoman(self):
        num = int(input("\n\n::: WELCOME TO INT TO ROMAN CONVERTER :::\n\nEnter number to convert : "))
        integers = [100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        # romans = ['C', 'L', 'X', 'V', 'I']

        converted = 'Roman number is : '

        i = 0
        while num > 0:
            for j in range(num // integers[i]):
                # print(f"i :{i}, j :{j}, value :{integers[i]}")
                converted += romans[i]
                num -= integers[i]
                # pass
            i += 1
        return converted

    def RomanToInt(self):
        # integers = [100, 50,10, 5, 1]
        # romans = ['C', 'L', 'X', 'V', 'I']
        # converted = 'Interger Number is : '
        s = input("Enter a roman number : ")
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            print(f"Range : {range(len(s))}, i : {i}")
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                # print("In IF condition ...")
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val


if __name__ == "__main__":
    obj1 = Numbers()
    obj2 = Numbers()

    # print(obj1.IntToRoman())
    print(obj2.RomanToInt())
