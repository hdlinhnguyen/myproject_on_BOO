using JuMP
import HiGHS
import MultiObjectiveAlgorithms as MOA

for i in 1:result_count(model)
    @assert is_solved_and_feasible(model; result = i)
    print(i, ": z = ", round.(Int, objective_value(model; result = i)), " | ")
    X = round.(Int, value.(x; result = i))
    print("Path:")
    for ind in findall(val -> val ≈ 1, X)
        i, j = ind.I
        print(" $i->$j")
    end
    println()
end
