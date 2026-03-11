facts = {"A", "B"}

rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E")
]

def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for premise, conclusion in rules:
            if premise.issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                changed = True
    return inferred


def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        return True

    if goal in visited:
        return False

    visited.add(goal)

    for premise, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(p, facts, rules, visited) for p in premise):
                return True

    return False


def resolve(ci, cj):
    resolvents = set()
    for di in ci:
        for dj in cj:
            if di == ('not', dj):
                new_clause = tuple(set(ci) - {di} | set(cj) - {dj})
                resolvents.add(new_clause)
            if dj == ('not', di):
                new_clause = tuple(set(ci) - {di} | set(cj) - {dj})
                resolvents.add(new_clause)
    return resolvents


def resolution(kb, query):
    clauses = kb + [(('not', query),)]
    new = set()

    while True:
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = resolve(clauses[i], clauses[j])
                if () in resolvents:
                    return True
                new = new.union(resolvents)

        if new.issubset(set(clauses)):
            return False

        for c in new:
            if c not in clauses:
                clauses.append(c)


print("Forward Chaining Result:", forward_chaining(facts, rules))

goal = "E"
print("Backward Chaining (Goal =", goal, "):", backward_chaining(goal, facts, rules))

kb = [
    ("A", "B"),
    (('not', "A"),),
]

query = "B"
print("Resolution proves query:", resolution(kb, query))