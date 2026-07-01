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
    
def ear(apr, n):
        """apr=名义年利率, n=每年复利次数"""
        return (1 + apr/n)**n - 1
def fv_annuity(C, r, n):
    """普通年金终值：每期末存入C，月利率r，共n期"""
    return C * ((1 + r)**n - 1) / r
def pv_annuity(C, r, n):
    return C * (1 - (1 + r)**(-n)) / r
    
calc = FinancialCalculator(r=0.05)
print(calc.fv(10000, 10))
print(calc.pv(20000, 3))

print(f"月复利 EAR: {ear(0.12, 12):.4f}")
print(f"日复利 EAR: {ear(0.12, 365):.4f}")
print(f"连续复利 EAR: {ear(0.12, 1000000):.4f}")

monthly_rate = 0.06 / 12
print(f"年金终值: {fv_annuity(1000, monthly_rate, 12):.2f}")

print(f"年金现值: {pv_annuity(1000, monthly_rate, 12):.2f}")