def eval_postfix(exp):
    s = []  # 파이썬 리스트를 스택으로 사용
    
    for ch in exp:
        # 공백은 건너뜀
        if ch == ' ':
            continue
            
        # 피연산자(숫자)인 경우
        if ch not in ('+', '-', '*', '/'):
            value = int(ch)  # ch - '0' 대신 int() 사용
            s.append(value)  # push
        # 연산자인 경우
        else:
            op2 = s.pop()  # 먼저 나오는 것이 오른쪽 피연산자
            op1 = s.pop()  # 나중에 나오는 것이 왼쪽 피연산자
            
            if ch == '+':
                s.append(op1 + op2)
            elif ch == '-':
                s.append(op1 - op2)
            elif ch == '*':
                s.append(op1 * op2)
            elif ch == '/':
                s.append(int(op1 / op2))  # 정수 나눗셈 처리
                
    return s.pop()

# 사용 예시: (3 + 4) * 2 -> 후위 표기법 "3 4 + 2 *"
print(eval_postfix("3 4 + 2 *"))  # 결과: 14