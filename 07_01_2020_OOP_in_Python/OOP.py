class Numbers:
    def IntToRoman(self):
        num = int(input("\n\n::: WELCOME TO INT TO ROMAN CONVERTER :::\n\nEnter number to convert : "))
        integers = [100, 90, 50, 40, 10, 9, 5, 4, 1]
        # romans = ['C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        romans = ['C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        converted = 'Roman number is : '

        i = 0
        while num > 0:
            # print(num//integers[i])
            for j in range(num // integers[i]):
                # print(f"i :{i}, j :{j}, value :{integers[i]}")
                converted += romans[i]
                num -= integers[i]
                # pass
            i += 1
        return converted

    def RomanToInt(self):
        integers = [100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        converted = 'Interger Number is : '



if __name__ == "__main__":
    obj1 = Numbers()
    print(obj1.IntToRoman())
