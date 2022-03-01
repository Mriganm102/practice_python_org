class truth_table(object):
    def __init__(self, propositional_formula):
        self.all_combinations = [(p,q) for p in [True,False] for q in [True ,False]]
        self.truth_table = [(p,q,propositional_formula(p,q)) for (p,q) in self.all_combinations]
    def display(self):
        print(self.__str__())
    def __str__(self):
        truth_table_string = ""
        for i, (p) in enumerate(self.truth_table):
            truth_table_string += (f"{i, (p)}\n")
        return truth_table_string
#def main():
#    def propositional_formula(p, q):
#        return (p and not p)
#    truth = truth_table(propositional_formula)
#    truth.display()
#if __name__ == '__main__':
#    main()
print("De Morgan's Laws")
class demorgan1(object):
    def __init__(self, propositional_formula):
        self.all_combinations = [(p,q) for p in [True, False] for q in [True, False]]
        self.truth_table = [(p, q, propositional_formula(p,q)) for (p,q) in self.all_combinations]
    def display(self):
        print(self.__str__())
    def __str__(self):
        truth_table_string = f"Index, (p, propositional_formula)\n"
        for i, (p) in enumerate(self.truth_table):
            truth_table_string += (f"{i, (p)}\n")
        return truth_table_string
def main():
    def propositional_formula(p, q):
        return (not (p and q))
    e31 = demorgan1(propositional_formula)
    e31.display()
if __name__ == '__main__':
    main()


class demorgan2(object):
    def __init__(self, propositional_formula):
        self.all_combinations = [(p,q) for p in [True, False] for q in [True, False]]
        self.truth_table = [(p, q, propositional_formula(p,q)) for p in self.all_combinations for q in self.all_combinations]
    def display(self):
        print(self.__str__())
    def __str__(self):
        truth_table_string = f"Index, (p, propositional_formula)\n"
        for i, (p) in enumerate(self.truth_table):
            truth_table_string += (f"{i, (p)}\n")
        return truth_table_string
def main():
    def propositional_formula(p, q):
        return (not p or not q)
    e31 = demorgan1(propositional_formula)
    e31.display()
if __name__ == '__main__':
    main()

print("Distributative Laws")
class distributative1(object):
    def __init__(self, propositional_formula, propositional_formula1):
        self.all_combinations = [(p,q,r) for p in [True, False] for q in [True, False] for r in [True, False]]
        self.truth_table = [(p, q, r, propositional_formula(p,q,r), propositional_formula1(p,q,r)) for (p,q,r) in self.all_combinations]
    def display(self):
        print(self.__str__())
    def __str__(self):
        truth_table_string = f"Index, (p, propositional_formula)\n"
        for i, (p) in enumerate(self.truth_table):
            truth_table_string += (f"{i, (p)}\n")
            assert p[-1] == p[-2]
        return truth_table_string
def main():
    def propositional_formula(p, q, r):
        return ((p or q) and r)
    def propositional_formula1(p, q, r):
        return ((p and r) or (q and r))
    e31 = distributative1(propositional_formula, propositional_formula1)
    e31.display()
if __name__ == '__main__':
    main()

class distributative2(object):
    def __init__(self, propositional_formula):
        self.all_combinations = [(p,q,r) for p in [True, False] for q in [True, False] for r in [True, False]]
        self.truth_table = [(p, q, r, propositional_formula(p,q,r)) for (p,q,r) in self.all_combinations]
    def display(self):
        print(self.__str__())
    def __str__(self):
        truth_table_string = f"Index, (p, propositional_formula)\n"
        for i, (p) in enumerate(self.truth_table):
            truth_table_string += (f"{i, (p)}\n")
        return truth_table_string
def main():
    def propositional_formula(p, q, r):
        return ((p and r) or (q and r))
    e31 = distributative2(propositional_formula)
    e31.display()
if __name__ == '__main__':
    main()


