from abc import ABC, abstractmethod
import re


class BasicFilter(ABC):
    @abstractmethod
    def check(self, text: str):
        pass

class RegexFilter(BasicFilter):
    terms: list[re.Pattern[str]] = []

    def load_from_file(self, path: str, manipulation: function[[str], str] = (lambda l: l)):
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    self.terms.append(manipulation(re.compile(line.lower())))

    def load_from_word_file(self, path: str, word_boundings=True):
        if word_boundings:
            def manipulation(line):
                return "\\b{line}\\b"
        else:
            def manipulation(line):
                return line
        self.load_from_file(path, manipulation)

    def check(self, text: str) -> bool:
        for word in self.terms:
            if word in text.lower():
                return True
        return False
    