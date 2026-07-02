"""
Distribution Explorer — 可视化模块（占位 / stub）

这里的函数现在还不能真正运行——它们要等 Python M7（Matplotlib）学完后才会实现。

这是一种叫"桩代码"（stub）的写法：先把函数的"接口"定下来（叫什么名字、
接收什么参数、该返回/画出什么），内部先用 NotImplementedError 占位。
好处是 main.py 未来调用这些函数时，名字和参数不用再改，只需要把
NotImplementedError 换成真正的实现。
"""


def plot_pmf(distribution, x_range):
    """
    绘制离散分布的概率质量函数（PMF）柱状图。

    参数：
        distribution: 一个分布对象（如未来的 Bernoulli / Binomial 类实例）
        x_range: 要绘制的 x 值范围
    """
    raise NotImplementedError("等 Python M7 学完 Matplotlib 后实现")


def plot_pdf(distribution, x_range):
    """绘制连续分布的概率密度函数（PDF）曲线。"""
    raise NotImplementedError("等 Python M7 学完 Matplotlib 后实现")


def plot_cdf(distribution, x_range):
    """绘制累积分布函数（CDF）曲线，离散/连续通用。"""
    raise NotImplementedError("等 Python M7 学完 Matplotlib 后实现")
