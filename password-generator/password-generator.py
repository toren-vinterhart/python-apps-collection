from abc import ABC, abstractmethod

import random
import string


class PasswordGeneratorAbstract(ABC):

    @abstractmethod
    def generate_password(self, length=8):
        pass


class NumericPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.digits

    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))
    

class LetterPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters

    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))


class MixedPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters + string.digits

    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))
    

generator = NumericPasswordGenerator()
print(generator.generate_password(20))

generator = LetterPasswordGenerator()
print(generator.generate_password(20))

generator = MixedPasswordGenerator()
print(generator.generate_password(20))
