"""
Distribution Explorer — 项目入口

一个交互式工具，用于探索概率分布的行为（参数扫描、对比、拟合真实数据）。

当前阶段：Week 1 脚手架
- 复用 Week 1 写的 SampleSpace（离散均匀概率模型）来验证项目结构是否打通
- 后续阶段会随课程进度逐步加入 Bernoulli / Binomial / Poisson / Normal 等真正的分布

路线图（对应 03-Capstone/distribution-explorer/README.md）：
- Phase 1（约Week 3-5，对应 SDT Ch.4-10）：实现离散/连续分布类，PMF/PDF/CDF
- Phase 2（约Week 6+）：MLE拟合、KS检验、AIC/BIC模型对比
- Phase 3（约Week 8-9）：CLT收敛动画、分布关系可视化
"""

import sys
from pathlib import Path

# Python 默认不知道 stats-distributions/src 在哪，需要手动把它加入搜索路径。
# Path(__file__) = 这个文件自己的路径；用 .parent 逐级往上走到仓库根目录，
# 再往下拼接到 stats-distributions/src。
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "stats-distributions" / "src"))

from probability_basics import SampleSpace


def demo():
    """验证跨模块导入是否成功：复用 Week 1 的 SampleSpace 做一次概率计算。"""
    dice = SampleSpace(range(1, 7))
    even = {2, 4, 6}
    high = {4, 5, 6}

    print("=== Distribution Explorer — Week 1 脚手架验证 ===")
    print(f"P(偶数) = {dice.P(even)}")
    print(f"P(大于3) = {dice.P(high)}")
    print(f"P(偶数 或 大于3) = {dice.inclusion_exclusion(even, high)}")


if __name__ == "__main__":
    demo()
