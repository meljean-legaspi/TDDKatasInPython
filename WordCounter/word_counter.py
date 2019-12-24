import re


class WordCounter:
    @staticmethod
    def count(words):
        words_list = re.findall(r'[\w]+', words)
        word_counter = ""
        for word in words_list:
            if word not in word_counter:
                word_counter += word + ", " + str(words.count(word))
                word_counter += "\n"
        return word_counter.strip('\n')
