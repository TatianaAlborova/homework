class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for p in punctuation:
                        line = line.replace(p, '')
                    words.extend(line.split())
                all_words[file_name] = words

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            word = word.lower()
            if word in words:
                position = words.index(word)
                result[file_name] = position + 1
                
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}

        word = word.lower()
        for file_name, words in all_words.items():
            count = words.count(word)
            result[file_name] = count

        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
