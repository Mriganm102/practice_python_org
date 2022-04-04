import logging
class quantifiers(object):
    def exists(self):
        truth_values = self.truth_values
        logging.warning(truth_values)
        return any(truth_values)




    def every(self):
        truth_values = self.truth_values
        logging.warning(truth_values)
        return all(truth_values)



    def unique(self):
        truth_values = self.truth_values
        y = 0
        for x in truth_values:
            if x == True:
                y = y + 1
        logging.warning(truth_values)
        if y == 1:
            return True
        else:
            return False


    def distinct(self):
        truth_values = self.truth_values
        y = 0
        for x in truth_values:
            if x == True:
                y = y + 1
        logging.warning(truth_values)
        if y > 1:
            return (True)
        else:
            return (False)


    def __init__(self):
        def propositional_formula(p, q):
            return ((p and q) or p)
        self.propositional_formula = propositional_formula
        all_combinations = [(p, q) for p in [True, False] for q in [True, False]]
        truth_table = [(p, q, propositional_formula(p, q)) for (p, q) in all_combinations]
        truth_values = ([three_tuple[2] for three_tuple in truth_table])
        self.all_combinations = all_combinations
        self.truth_table = truth_table
        self.truth_values = truth_values
        print(self.exists())
        print(self.every())
        print(self.unique())
        print(self.distinct())

def main():
    quant = quantifiers()
if __name__ == '__main__':
    main()