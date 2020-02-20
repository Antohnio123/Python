class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self, when):
        self.when = 'I`m not ready yet'


Jon = Man('Jon')
print(Jon.name)
Jon.solve_task(None)
print(Jon.when)
