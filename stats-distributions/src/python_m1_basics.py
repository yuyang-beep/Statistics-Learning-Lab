# Python M1 — 数据类型 & 控制流

# === 基本类型 ===
n = 5          # int
pi = 3.14      # float
name = "MindOS"  # str
flag = True    # bool

# === 容器类型 ===
scores = [85, 90, 78, 95, 88]   # list - 用下标取值
omega = {1, 2, 3, 4, 5, 6}      # set  - 无重复，支持集合运算
student = {"姓名": "吴宇洋", "年级": 2}  # dict - 用键取值

# === 控制流 ===
def classify_r2(r2):
    if r2 > 0.9:
        return "优秀"
    elif r2 > 0.6:
        return "一般"
    else:
        return "差"

# === for 循环 ===
total = sum(score for score in scores)
avg = total / len(scores)
print(f"平均分: {avg}")
print(f"R²评级: {classify_r2(0.9917)}")