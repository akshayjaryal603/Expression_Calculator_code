#Calculator Program

class ConversionAndEvalute:

    def __init__(self):
        self.top = -1
        self.capacity = 1000
        self.array = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        if isinstance(ch, int):
            return True

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # The main function that converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)

            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while ((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        while not self.isEmpty():
            self.output.append(self.pop())

        return self.output

    def evaluatePostfix(self, exp):

        for i in exp:

            if isinstance(i, int):
                self.push(i)

            else:
                val1 = self.pop()
                val2 = self.pop()
                if i=="+":
                    self.push(str(float(val2) + float(val1)))
                elif i=="-":
                    self.push(str(float(val2) - float(val1)))
                elif i=="*":
                    self.push(str(float(val2) * float(val1)))
                elif i=="/":
                    self.push(str(float(val2) / float(val1)))
                else:
                    print("Invalid operator")

        return float(self.pop())

exp = input("Enter your Expression : ")
e=""
for i in exp:
    if i==" ":
        continue
    else:
        e=e+i
st=e
listt=[]
ln=len(st)
i=0
while i<ln:
    if st[i].isdigit():
        tmp=""
        while i<ln and st[i].isdigit():
            tmp=tmp+st[i]
            i+=1
        listt.append(int(tmp))
    else:
        listt.append(st[i])
        i=i+1
ex=listt
obj = ConversionAndEvalute()
postfixExpression=obj.infixToPostfix(ex)
print (">>>> ",postfixExpression)
print (obj.evaluatePostfix(postfixExpression))

