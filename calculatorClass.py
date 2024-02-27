class Calculator:
    def __init__(self, firstNum: int, secondNum: int, operator: str) -> None:
        self.firstNum = firstNum
        self.secondNum = secondNum
        self.operator = operator

    def addNum(self) -> int:
        if self.operator == "+":
            return self.firstNum + self.secondNum
        
    def subtractNum(self) -> int:
        if self.operator == "-":
            return self.firstNum - self.secondNum
        
    def multiplyNum(self) -> int:
            if self.operator == "*":
                return self.firstNum * self.secondNum
            
    def divideNum(self) -> int:
            if self.operator == "/":
                return self.firstNum / self.secondNum

    def raiseToPowNum(self) -> int:
            if self.operator == "^":
                return self.firstNum ** self.secondNum
    def toPercentPowNum(self) -> int:
            if self.operator == "%":
                return self.firstNum / 100

calcObj = Calculator(2,2,"^")
print(calcObj.raisePowNum())
