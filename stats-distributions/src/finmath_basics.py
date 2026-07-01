import math

P = 10000
r = 0.05
t = 10

annual     = P * (1 + r)**t
monthly    = P * (1 + r/12)**(12*t)
continuous = P * math.exp(r * t)

print(f"年复利:   {annual:.2f}")
print(f"月复利:   {monthly:.2f}")
print(f"连续复利: {continuous:.2f}")

def present_value(C, r, n):
    """离散复利现值"""
    return C / (1 + r)**n

def present_value_continuous(C, r, t):
    """连续复利现值"""
    return C * math.exp(-r * t)

n = 3
t = 3
C = 20000
r = 0.05

pv_discrete = present_value(C, r, n)
pv_continuous = present_value_continuous(C, r, t)
print(f"离散复利现值: {pv_discrete:.2f}")
print(f"连续复利现值: {pv_continuous:.2f}")

class FinancialCalculator:
    def __init__(self, r):
        self.r = r

    def fv(self, P, t, n=1):
        """终值：P 今天存入，t年后"""
        return P * (1 + self.r / n) ** (n * t)

    def fv_continuous(self, P, t):
        return P * math.exp(self.r * t)

    def pv(self, C, t, n=1):
        """现值：t年后收到 C，今天值多少"""
        return C / (1 + self.r / n) ** (n * t)

    def pv_continuous(self, C, t):
        return C * math.exp(-self.r * t)
    
calc = FinancialCalculator(r=0.05)
print(calc.fv(10000, 10))
print(calc.pv(20000, 3))