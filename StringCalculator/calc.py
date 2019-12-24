import re


class StringCalculator:
    @staticmethod
    def add(numbers):
        sum_of_input = 0

        if numbers != "":
            if "//" in numbers:
                delimiter = numbers[numbers.rfind('/') + 1]
                numbers = str.replace(numbers, "//", "")
                numbers = str.replace(numbers, "\n", "")
                addends = re.split(delimiter, numbers)
                addends.remove('')
            else:
                addends = re.findall(r'[\d]+', numbers)
            for addend in addends:
                sum_of_input += int(addend)

        return sum_of_input
