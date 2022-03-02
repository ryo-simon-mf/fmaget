import markovify
import MeCab

text_file = open('test.txt', 'r')
text = text_file.read()

parsed_text = MeCab.Tagger('-Owakati').parse(text)


text_model = markovify.Text(parsed_text, state_size = 2)

for _ in range(10):
    sentence = text_model.make_short_sentence(100, 20, tries = 100).replace(' ', '')
    print(sentence)
