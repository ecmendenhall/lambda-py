# encoding: utf-8
import readline


def tokenize(string):
    for symbol in ['(', ')', '.']:
        string = string.replace(symbol, ' ' + symbol + ' ')
    return string.split()


class LambdaPySyntaxError:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def parse(s_exp):
    def parse_tokens(tokens, exp_open):
        if len(tokens) == 0:
            raise SyntaxError('unexpected EOF while reading')
        exp = tuple()
        while len(tokens) > 0:
            token = tokens.pop(0)
            if token == '(':
                exp += (parse_tokens(tokens, True),)
            elif token == ')':
                if exp_open:
                    return exp
                else:
                    raise LambdaPySyntaxError('Unmatched close parentheses')
                    return None
            else:
                exp += atomize(token)

        if exp_open:
            raise LambdaPySyntaxError('Unmatched open parentheses')
            return None
        else:
            return exp

    return parse_tokens(tokenize(s_exp), False)


def atomize(token):
    if token in 'abcdefghijklmnopqrstuvwxyz':
        return (token, )
    if token[0] == u'\u03bb':
        return ('lambda', token[1])
    else:
        return ()


def new_container(container_type, contents=None):
    if contents:
        if container_type == 'list':
            return list() + [contents]
        elif container_type == 'tuple':
            return tuple() + (contents,)
    else:
        if container_type == 'list':
            return list()
        elif container_type == 'tuple':
            return tuple()


def walkmap(func, container):
    container_type = type(container).__name__
    mapped = new_container(container_type)
    for element in container:
        if hasattr(element, '__iter__'):
            mapped += new_container(container_type,
                                    walkmap(func, element))
        else:
            mapped += new_container(container_type,
                                    func(element))
    return mapped


def walkfilter(func, container):
    container_type = type(container).__name__
    filtered = new_container(container_type)
    for element in container:
        if hasattr(element, '__iter__'):
            filtered += new_container(container_type,
                                      walkfilter(func, element))
        else:
            if func(element):
                filtered += new_container(container_type,
                                          element)
    return filtered


def walkreduce(func, container):
    container_type = type(container).__name__
    reduced = new_container(container_type)
    for element in container:
        if hasattr(element, '__iter__'):
            reduced += walkreduce(func, element)
        else:
            if func(element):
                reduced += new_container(container_type,
                                         element)
    return reduced


def replace(el, a, b):
    if el == a:
        return b
    else:
        return el


def free(exp):
    return set(walkreduce(lambda x: type(x).__name__ == 'unicode',
                          walkfilter(lambda x: (x not in bound(exp) and
                                                x != 'lambda'),
                                      exp)))


def bound(exp):
    def get_bound(exp):
        bound_vars = []
        if type(exp).__name__ != 'tuple':
            return []
        elif exp[0] == 'lambda':
            lhs = exp[1]
            rhs = exp[2]
            bound_vars.append(lhs)
            return bound_vars + get_bound(rhs)
        else:
            for var in exp:
                bound_vars += get_bound(var)
            return bound_vars

    return set(get_bound(exp))


def apply(lambda_exp, var):
    pass


def beta_reduce(lhs, rhs, param):
    pass


def interpret(ast):
    operator = ast[0]

    if type(operator) is not str:
        operator = interpret(operator)

    # Abstraction
    elif operator == 'lambda':
        pass


def read_input(prompt='λpy>>> '):
    user_input = raw_input(prompt)
    exp = unicode(user_input, 'utf-8')
    try:
        r = parse(exp)
        print r
        interpret(r)
    except LambdaPySyntaxError:
        read_input()


def repl():
    readline.parse_and_bind(';: "λ"')

    while True:
        read_input()
