from arraystack import ArrayStack
class Palindrome:
    def __init__(self, name):
        self.name = name


    def read_file(self):
        words = []
        new_words = []
        i = 0
        letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        file = open(self.name, 'r', encoding='UTF-8')
        for line in file:
            line = line.strip().split()
            words.append(line)
        for lst in words:
            if len(lst) > 1:
                del lst[1:]
            for w in lst:
                new_words.append(w)
        print(new_words)
        return new_words

    def check_word(self):
        reverse = ''
        lst = []
        stack = ArrayStack()
        words = self.read_file()
        for word in words:
            for letter in word:
                stack.add(letter)
            while len(stack) != 0:
                reverse += stack.pop()
            if word == reverse:
                lst.append(word)
            reverse = ''
        return lst

    def write_in_file(self, write_file):
        self.write_file = write_file
        polindrome = self.check_word()
        file = open(self.write_file, 'w')
        for pol in polindrome:
            file.write(pol + '\n')

pol = Palindrome('base.lst')
pol.write_in_file('palindrome_uk.txt')
