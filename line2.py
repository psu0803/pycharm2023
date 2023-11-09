from stack import stack
from precedence import precedence
def line2(expr):
    s = stack(100)
    output = []

    for term in expr :
        if term in '(':
            s.push('(')

        elif term in ')':
            while not s.isEmpty() :
                op = s.pop()
                if op=='(' :
                    break;
                else :
                    output.append(op)

        elif term in "+-*/" :
            while not s.isEmpty() :
                op = s.peek()
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)

        else:
            output.append(term)

    while not s.isEmpty() :
        output.append(s.pop())

    return output