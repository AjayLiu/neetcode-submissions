class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        operands = []
        for token in tokens:
            # print(operands)
            if token in operators:
                op1 = int(operands.pop())
                op2 = int(operands.pop())
                match (token):
                    case '+':
                        operands.append(op1 + op2)
                    case '-':
                        operands.append(op2 - op1)
                    case '*':
                        operands.append(op2 * op1)
                    case '/':
                        operands.append(op2 / op1)
            else:
                operands.append(token)
        return int(operands[0])