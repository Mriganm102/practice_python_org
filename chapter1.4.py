import logging


def exists():
    def propositional_formula(p, q):
        return ((p and q) or p)
    all_combinations = [(p, q) for p in [True, False] for q in [True, False]]
    truth_table = [(p, q, propositional_formula(p,q)) for (p, q) in all_combinations]
    truth_values = ([three_tuple[2] for three_tuple in truth_table])
    logging.warning(truth_values)
    logging.warning(any(truth_values))


exists()

def every():
    def propositional_formula(p, q):
        return ((p and q) or p)
    all_combinations = [(p, q) for p in [True, False] for q in [True, False]]
    truth_table = [(p, q, propositional_formula(p, q)) for (p, q) in all_combinations]
    truth_values = ([three_tuple[2] for three_tuple in truth_table])
    logging.warning(truth_values)
    logging.warning(all(truth_values))

every()

def unique():
    def propositional_formula(p, q):
        return ((p and q) or p)
    all_combinations = [(p, q) for p in [True, False] for q in [True, False]]
    truth_table = [(p, q, propositional_formula(p, q)) for (p, q) in all_combinations]
    truth_values = ([three_tuple[2] for three_tuple in truth_table])
    y = 0
    for x in truth_values:
        if x == True:
            y = y + 1
    logging.warning(truth_values)
    if y == 1:
        logging.warning(True)
    else:
        logging.warning(False)
unique()

def distinct():
    def propositional_formula(p, q):
        return ((p and q) or p)
    all_combinations = [(p, q) for p in [True, False] for q in [True, False]]
    truth_table = [(p, q, propositional_formula(p, q)) for (p, q) in all_combinations]
    truth_values = ([three_tuple[2] for three_tuple in truth_table])
    y = 0
    for x in truth_values:
        if x == True:
            y = y + 1
    logging.warning(truth_values)
    if y > 1:
        logging.warning(True)
    else:
        logging.warning(False)
distinct()
