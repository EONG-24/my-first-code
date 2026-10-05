def precedence(self, op):
    """연산자의 우선순위를 반환하는 메서드"""
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(self, expression):
    """중위 표기식을 후위 표기식으로 변환하는 메서드"""
    self.stack = []  # 괄호, 연산자를 담을 스택
    self.output = []  # 후위 표기식을 담을 리스트
    expression = self.tokenization(expression)

    for token in expression:
        if self.is_operand(token):
            self.output.append(token)
        elif token == '(':
            self.stack.append(token)
        elif token == ')':
            while self.stack and self.stack[-1] != '(':
                self.output.append(self.stack.pop())
            self.stack.pop()  # pop '('
        else:  # Operator (연산자인 경우)
            while self.stack and self.precedence(self.stack[-1]) >= self.precedence(token):
                self.output.append(self.stack.pop())
            self.stack.append(token)

    # 스택에 남아있는 나머지 연산자 모두 pop
    while self.stack:
        self.output.append(self.stack.pop())

    return "".join(self.output)