import random
import parser


class Test:
    def __init__(self):
        self.i = random.choice(parser.Data().addData())[0]

    def getTest(self):
        return self.i

    @staticmethod
    def check(model, x):
        result = ["X"] * 5
        for i in range(0, 5):
            if model[i] == x[i]:
                result[i] = "G"

        for i in range(0, 5):
            if result[i] != "G":
                if x[i] in model:
                    result[i] = "E"
        return result
