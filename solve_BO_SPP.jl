using JuMP
using Gurobi 
import MultiObjectiveAlgorithms as MOA
M = 50
C1 = [
    M 4 5 M M M
    M M 2 1 2 7
    M M M 5 2 M
    M M 5 M M 3
    M M M M M 4
    M M M M M M
]
C2 = [
    M 3 1 M M M
    M M 1 4 2 2
    M M M 1 7 M
    M M 1 M M 2
    M M M M M 2
    M M M M M M
]
n = size(C2, 1)
model = Model(Gurobi.Optimizer)
set_silent(model)
@variable(model, x[1:n, 1:n], Bin)
@objective(model, Min, [sum(C1 .* x), sum(C2 .* x)])
@constraint(model, sum(x[1, :]) == 1)
@constraint(model, sum(x[:, n]) == 1)
@constraint(model, [i = 2:n-1], sum(x[i, :]) - sum(x[:, i]) == 0)
set_optimizer(model, () -> MOA.Optimizer(Gurobi.Optimizer))
set_attribute(model, MOA.Algorithm(), MOA.EpsilonConstraint())
optimize!(model)
solution_summary(model)
objective_value(model; result=4)
