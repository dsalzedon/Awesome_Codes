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


def get_freq(lst):
    uninteresting_words = ["a", "the", "I", "if", "to", "and", "am", "was", "is", "are", "be", "i", "of", "that", "this"]
    words_frequency = {}

    for x in wrds:
        if x.lower() not in uninteresting_words:
            if x.lower() not in words_frequency:
                words_frequency[x.lower()] = 1
            else:
                words_frequency[x.lower()] += 1

    return words_frequency


text_path = "theraven.txt"
font_path = "/System/Library/Fonts/HelveticaNeue.ttc"

wrds = get_wrds(text_path)

words_frequency = get_freq(wrds)

file_name = text_path.split(".txt")[0]

cloud = wordcloud.WordCloud(font_path=font_path, width=800, height=400, margin=5, font_step=5, contour_width=100, background_color='black', colormap="plasma")
cloud.generate_from_frequencies(words_frequency)
cloud.to_file(f"img/{file_name}.jpg")
