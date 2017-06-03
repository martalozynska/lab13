from arraystack import ArrayStack
class Palindrome:
    def __init__(self, name):
        self.name = name

    def read_file(self):
        words = []
        file = open(self.name, 'r')
        for line in file:
            line = line.strip()
            words.append(line)
        return words

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

palindrome1 = Palindrome('words.txt')
palindrome1.write_in_file('palindrome_en.txt')
