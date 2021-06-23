import random

answers = ["Yes definitely.", "As I see it, yes.", "Ask again later.", "Cannot predict now.", "Don't count on it.", "Very doubtful.", "It is certain.", " Concentrate and ask again.","You may rely on it.", "Better not tell you now."]

i = random.choice(answers)

input("Ask a question:")
print(i)