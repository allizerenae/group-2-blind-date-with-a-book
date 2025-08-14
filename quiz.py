
###################################################################
# 2. Average Words Length

# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.


def solution2(sentence):

    cleaned = sentence.translate(str.maketrans('', '', string.punctuation))

    words = cleaned.split()

    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)



sentence1 = "Hi class, we are practicing solving algorithms. It is fun, don't you think?.."
sentence2 = "We need to work very hard to learn more about algorithms!"

print(solution2(sentence1))
print(solution2(sentence2))
