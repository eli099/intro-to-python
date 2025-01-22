# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
    print("words ->", words)
    # function to filter out words without dashes & longer than 10 characters
    whole = remove_dashed_words(words)
    print("whole ->", whole)
    # mapping function to shorten words longer than 15 charcters & add elipses
    shorter = shorten_words(whole)
    print("shorter ->", shorter)
    # return "These words are quite long: ...""
    print("These words are quite long:" + ", ".join(shorter))
    return "These words are quite long: " + ", ".join(shorter)
    
# function to filter out words without dashes & longer than 10 characters
def remove_dashed_words(words):
    whole_words = []
    for word in words:
        if "-" not in word and len(word) > 10:
            print(f"{word} is more than 10 characters \n")
            whole_words.append(word)
        else:
            print(f"'{word}' is 10 characters or less or contains dashes \n")
    print("whole_words 1 ->", whole_words)
    return whole_words

# mapping function to shorten words longer than 15 charcters & add elipses
def shorten_words(whole_words):
    short_words = []
    for word in whole_words:
        if len(word) > 15:
            shortened = word[0:15] + "..."
            short_words.append(shortened)
        else:
            short_words.append(word)
    print("short_words ->", short_words)
    return short_words
            
            

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
