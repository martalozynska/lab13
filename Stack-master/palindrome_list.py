from arraystack import ArrayStack
class Palindrome:
    def __init__(self, name):
        '''
        Initialazes the name of the file where the data is.
        :param name: the name of the file where the data is.
        '''
        self.name = name


    def read_file(self):
        '''
        Reads the file where the data is located.
        :return: list of words
        :return:
        '''
        words = []
        new_words = []
        file = open(self.name, 'r', encoding='UTF-8')
        for line in file:
            line = line.strip().split()
            words.append(line)
        for lst in words:
            if len(lst) > 1:
                del lst[1:]
            for w in lst:
                new_words.append(w)
        #print(new_words)
        return new_words

    def check_word(self):
        '''
        Function checks words from the list if they are palindromes.
        :return: list of palindromes.
        '''
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
        '''
        Function writes palindromes to the file.
        :param write_file: name of the file.
        :return:
        '''
        self.write_file = write_file
        polindrome = self.check_word()
        file = open(self.write_file, 'w')
        for pol in polindrome:
            file.write(pol + '\n')

pol = Palindrome('words.txt')
print(pol.write_in_file('palindrome_en.txt'))
