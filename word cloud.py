import wordcloud


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


path = "theraven.txt"
uninteresting_words = ["a", "the", "I", "if", "to", "and", "am", "was", "is", "are", "be"]    

wrds = get_wrds(path)

words_frequency = {}

for x in wrds:
    if x not in uninteresting_words:
        if x not in words_frequency:
            words_frequency[x] = 1
        else:
            words_frequency[x] += 1

file_name = path.split(".txt")[0]

cloud = wordcloud.WordCloud(width=400, height=800, margin=5, font_step=5, contour_width=100)
cloud.generate_from_frequencies(words_frequency)
cloud.to_file(f"{file_name}.jpg")
