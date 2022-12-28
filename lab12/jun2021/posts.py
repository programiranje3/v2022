from datetime import datetime as dt
from random import randint
from sys import stderr
import json_tricks


class Post:

    dt_format = "%d-%m-%Y %H:%M:%S"

    def __init__(self, username, content):
        self.username = username
        self.content = content
        self.timestamp = dt.now()
        self.id = randint(100000, 1000000)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value and isinstance(value, str) and len(value) >= 4 and value[0].isalpha() and value[1:].isalnum():
            self.__username = value
        else:
            self.__username = None
            raise ValueError(f"The input value ({value}) does not conform to the requirements for username\n")

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        if isinstance(value, dt):
            self.__timestamp = value
        elif isinstance(value, str):
            try:
                self.__timestamp = dt.strptime(value, Post.dt_format)
            except ValueError as err:
                stderr.write(f"Error when setting timestamp - incorrect datetime format\n{err}\n")
        else:
            self.__timestamp = None
            stderr.write(f"Error - wrong input ({value}), timestamp cannot be set\n")

    def __str__(self):
        post_str = f"Post id:{self.id}\nSent by: {self.username}\nTimestamp: {self.timestamp}\n"
        post_str += f"Content: {self.get_up_to_10_words(self.content)}"
        return post_str

    @staticmethod
    def get_up_to_10_words(text):
        if not text:
            return ""
        words = text.split()
        return text if len(words) <= 10 else (" ".join(words[:10]) + "...")


class Question(Post):

    def __init__(self, username, content, title, tags=None):
        super().__init__(username, content)
        self.title = title
        self.tags = tags if tags else list()
        self.responses = list()

    def __str__(self):
        lines = super().__str__().split('\n')
        lines[0] = lines[0].replace("Post", "Question")
        lines.insert(3, f"Title: {self.title}")
        lines.append(f"Tags: {'none' if len(self.tags)==0 else ','.join(self.tags)}")
        responses_str = 'none' if len(self.responses)==0 else '\n'.join([str(response) for response in self.responses])
        lines.append(f"Responses:\n{responses_str}")
        return '\n'.join(lines)

    def response_generator(self, threshold):
        try:
            threshold_dt = dt.strptime(threshold, '%d/%m/%Y')
        except ValueError as err:
            raise RuntimeError(f"Error - the input argument is not in the requested format:\n{err}\n")
        else:
            selection = [response for response in self.responses if response.timestamp > threshold_dt]
            if len(selection) == 0:
                print(f"No responses after {threshold}; the available responses are given below")
                selection = self.responses
            for response in sorted(selection, key=lambda r: r.votes, reverse=True):
                yield response


class Answer(Post):

    def __init__(self, username, content):
        super().__init__(username, content)
        self.votes = 0
        self.accepted = False

    def __str__(self):
        lines = super().__str__().split('\n')
        lines[0] = lines[0].replace("Post", "Answer")
        lines.append(f"Votes: {self.votes}")
        lines.append(f"Accepted: {self.accepted}")
        return "\n".join(lines)

    @property
    def accepted(self):
        return self.__accepted

    @accepted.setter
    def accepted(self, value):
        if isinstance(value, bool):
            self.__accepted = value
        elif isinstance(value, str) and value.lower() in ['true', 'false']:
            self.__accepted = True if value.lower() == 'true' else False
        else:
            stderr.write(f"Incorrect value for the accepted attribute -> value assignment cannot be done\n")


def to_json(obj, fpath):
    try:
        with open(fpath, 'w') as fobj:
            json_tricks.dump(obj, fobj, indent=4)
    except OSError as err:
        stderr.write(f"The following error occurred while writing to {fpath}\n{err}\n")


def from_json(fpath):
    try:
        with open(fpath, 'r') as fobj:
            return json_tricks.load(fobj)
    except FileNotFoundError:
        stderr.write(f"File {fpath} cannot be found\n")
    except OSError as err:
        stderr.write(f"The following error occurred while reading from {fpath}\n{err}\n")
