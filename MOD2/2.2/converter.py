class Converter:
    def __init__(self, roman_to_decimal, decimal_to_roman):
        self.roman_to_decimal = roman_to_decimal
        self.decimal_to_roman = decimal_to_roman

    def convert(self, source, value):
        if source == 'decimal':
            return self.decimal_to_roman(value)
        else:
            return self.roman_to_decimal(value)


class RomanNumericConverter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
            'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
        }
        self.decimal_numerals = {v: k for k, v in self.roman_numerals.items()}

    def roman_to_decimal(self, s: str) -> int:
        total, prev = 0, 0
        for c in reversed(s):
            if (value := self.roman_numerals[c]) >= prev:
                total += value
            else:
                total -= value
            prev = value
        return total

    def decimal_to_roman(self, num: int) -> str:
        result = ''
        for value in sorted(self.decimal_numerals.keys(), reverse=True):
            while num >= value:
                result += self.decimal_numerals[value]
                num -= value
        return result


if __name__ == '__main__':
    roman_converter = RomanNumericConverter()
    converter = Converter(roman_converter.roman_to_decimal, roman_converter.decimal_to_roman)

    while True:
        print("\n1. Convert Roman to Decimal")
        print("2. Convert Decimal to Roman")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            roman = input("Enter Roman number: ")
            print(f"Decimal representation: {converter.convert('roman', roman)}")
        elif choice == '2':
            decimal = int(input("Enter Decimal number: "))
            print(f"Roman representation: {converter.convert('decimal', decimal)}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
