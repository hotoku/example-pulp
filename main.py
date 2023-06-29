#!/usr/bin/env python


from typing import Any
import pulp


def main() -> None:
    # 問題の定義
    problem = pulp.LpProblem(name="Diet", sense=pulp.LpMinimize)

    # 変数の定義
    x: list[Any] = [None] * 3
    x[0] = pulp.LpVariable(name="x[0]", lowBound=0, cat="Integer")
    x[1] = pulp.LpVariable(name="x[1]", lowBound=0, cat="Integer")
    x[2] = pulp.LpVariable(name="x[2]", lowBound=0, cat="Integer")

    # 目的関数
    problem += 20*x[0] + 12*x[1] + 18*x[2]

    # 制約条件の定義
    problem += 22*x[0] + 13*x[1] + 17*x[2] >= 200
    problem += 20*x[0] + 30*x[1] + 5*x[2] >= 200
    problem += 10*x[0] + 5*x[1] + 12*x[2] >= 100

    # 解く
    status = problem.solve()
    print(pulp.LpStatus[status])

    # 結果表示
    print("Result")
    print("x[0]:", x[0].value())
    print("x[1]:", x[1].value())
    print("x[2]:", x[2].value())


if __name__ == "__main__":
    main()
