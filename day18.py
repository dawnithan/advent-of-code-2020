# https://gist.github.com/nitely/497540eb017ed8a75aecb6a4e609c9a2

import collections

RIGHT, LEFT = range(2)

Op = collections.namedtuple('Op', [
    'precedence',
    'associativity'])

# in day 18, every operator has the *same* precedence except for part 2, where add > mult
OPS = {
    '^': Op(precedence=2, associativity=RIGHT),
    '*': Op(precedence=2, associativity=LEFT),
    '/': Op(precedence=2, associativity=LEFT),
    '+': Op(precedence=3, associativity=LEFT),
    '-': Op(precedence=3, associativity=LEFT)}


def has_precedence(a, b):
    return ((OPS[b].associativity == RIGHT and
             OPS[a].precedence > OPS[b].precedence) or
            (OPS[b].associativity == LEFT and
             OPS[a].precedence >= OPS[b].precedence))


def _pop_greater_than(ops, op):
    out = []

    while True:
        if not ops:
            break

        if ops[-1] not in OPS:
            break

        if not has_precedence(ops[-1], op):
            break

        out.append(ops.pop())

    return out


def _pop_until_group_start(ops):
    out = []

    while True:
        op = ops.pop()

        if op == '(':
            break

        out.append(op)

    return out


def rpn(expression):
    """
    An implementation of the Shunting-yard algorithm\
    for producing Reverse Polish notation out of\
    an expression specified in infix notation
    """
    output = []
    operators = []

    for char in expression:
        if char == '(':
            operators.append(char)
            continue

        if char == ')':
            output.extend(_pop_until_group_start(operators))
            continue

        if char in OPS:
            output.extend(_pop_greater_than(operators, char))
            operators.append(char)
            continue

        if char.isdigit():
            output.append(char)

    output.extend(reversed(operators))

    return ''.join(output)

ops = ['+', '*']
total = 0

with open("day18-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

for expression in data:
    postfix = rpn(expression)
    stack = []

    for t in postfix:
        if t in ops:
            y = int(stack.pop())
            x = int(stack.pop())
            if t == '+':
                stack.append(x + y)
            elif t == '*':
                stack.append(x * y)
        else:
            stack.append(int(t))

    total += stack.pop()

print(total)