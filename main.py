class AbstractFrequencyCounter:
    def __init__(self, address):
        self.address = address

    def calculateFreqs(self):
        pass


class ListCount(AbstractFrequencyCounter):
    def calculateFreqs(self):
        result = []
        with open(self.address, 'r') as file:
            text = file.read().lower()
        for letter in range(ord('a'), ord('z') + 1):
            count = text.count(chr(letter))
            result.append(f"{chr(letter)} = {count}")
        print(result)


class DictCount(AbstractFrequencyCounter):
    def calculateFreqs(self):
        result = {}
        with open(self.address, 'r') as file:
            text = file.read().lower()
        for letter in range(ord('a'), ord('z') + 1):
            count = text.count(chr(letter))
            result[chr(letter)] = count
        print(result)


# create objects and test
list_count_obj = ListCount('weirdWords.txt')
list_count_obj.calculateFreqs()

dict_count_obj = DictCount('weirdWords.txt')
dict_count_obj.calculateFreqs()
