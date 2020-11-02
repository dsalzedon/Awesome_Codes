import wordcloud


path = "theraven.txt"
uninteresting_words = ["a", "the", "I", "if", "to", "and", "am", "was", "is", "are", "be"]


def get_wrds(path):
    words = ""
    with open(path, "r") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    words = words + str(char)
                elif char == " ":
                    words = words + " "
            words = words + " "
        return words.split()


wrds = get_wrds(path)

words_frequency = {}

for x in wrds:
    if x not in words_frequency and x not in uninteresting_words:
        words_frequency[x] = 1
    else:
        if x not in uninteresting_words:
            words_frequency[x] += 1

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(words_frequency)
cloud.to_file("myfile.jpg")
