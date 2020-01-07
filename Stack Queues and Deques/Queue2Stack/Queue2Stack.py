class Queue2Stack(object):

    def __init__(self):
        self.income = []
        self.outcome = []

    def enqueue(self, element):
        self.income.append(element)

    def dequeue(self):
        if not self.outcome:
            while self.income:
                self.outcome.append(self.income.pop())
        return self.outcome.pop()
