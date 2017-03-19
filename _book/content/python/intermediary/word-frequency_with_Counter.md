from collections import Counter

text = 'We hope to one day become the world\'s leader in free, educational resources. ' \
       'We are constantly discovering and adding more free content to the website everyday.' \
       'There is already an enormous amount of resources online that can be accessed for free ' \
       'by anyone in the world, the main issue right now is that very little of it is organized ' \
       'or structured in any way. We want to be the solution to that problem.'

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3) # Gets me the three most common words in the text

print(top_three)