def bayes(p_b, p_a_given_b, p_a_given_not_b):
    """
    p_b           = P(B)      先验概率
    p_a_given_b   = P(A|B)    似然
    p_a_given_not_b = P(A|Bᶜ) 误报率
    返回 P(B|A)
    """
    p_not_b = 1-p_b
    p_a     = p_b*p_a_given_b + p_not_b*p_a_given_not_b
    return p_b*p_a_given_b / p_a

# 测试：医疗诊断场景
print(bayes(0.3, 0.8, 0.1))  # 应该输出 0.774...
print(bayes(0.01, 0.8, 0.1))