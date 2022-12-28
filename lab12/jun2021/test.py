from posts import Question, Answer, Post, to_json, from_json
from pathlib import Path

# text = "History in the making! @vay_io will be the first company to put a passenger vehicle without a driver " \
#        "inside on public roads in Europe! Here’s a small teaser from our testing ground at #tegel, #berlin. " \
#        "Beginning of 2023 will be legendary!"
# p = Post('bdjukic', text)
# print(p)

q1 = Question('jan1',
              'As far as I understand, in Python, '
              'comparing the instances of two different classes for equality, does:...',
              'Python: Raise error when comparing objects of different type for equality',
              ['python', 'error', 'object-comparison'])
# print(q1)
# print()

a1 = Answer('Fredrik',
            'To check if o is an instance of str or any subclass of str, use isinstance '
            '(this would be the "canonical" way)')
a1.votes = 10
a1.accepted = True

a2 = Answer('DanLenski',
            'The most Pythonic way to check the type of an object is... not to check it.')
a2.votes = 5

q1.responses.extend([a1, a2])

# print(q1)
# print()

# print("\nResponses after 23/12/2022:")
# for r in q1.response_generator("23/12/2022"):
#     print(r)

q2 = Question("Mat1",
              "What is __init__.py for in a Python source directory?",
              "What is __init__.py for?",
              ['python', 'module', 'package'])

to_json([q1, q2], Path.cwd() / "questions.json")

print("\nQuestions read from json file:")
questions = from_json(Path.cwd() / "questions.json")
for q in questions:
    print(q)
    print()