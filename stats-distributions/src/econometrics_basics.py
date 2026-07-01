def ols(x, y):
    n = len(x)
    x_bar = sum(x) / n
    y_bar = sum(y) / n
    
    beta1 = sum((x[i]-x_bar)*(y[i]-y_bar) for i in range(n)) / sum((x[i]-x_bar)**2 for i in range(n))
    beta0 = y_bar - beta1 * x_bar
    
    return beta0, beta1

x = [50, 60, 70, 80, 90]
y = [150, 180, 210, 230, 270]

b0, b1 = ols(x, y)
print(f"截距 β₀ = {b0:.2f}")
print(f"斜率 β₁ = {b1:.2f}")

def r_squared(x, y, beta0, beta1):
    y_bar = sum(y) / len(y)
    y_hat = [beta0 + beta1 * x[i] for i in range(len(x))]
    
    ss_res = sum((y[i] - y_hat[i])**2 for i in range(len(y)))  # 残差平方和
    ss_tot = sum((y[i] - y_bar)**2 for i in range(len(y)))     # 总平方和
    
    return 1 - ss_res / ss_tot

print(f"R² = {r_squared(x, y, b0, b1):.4f}")