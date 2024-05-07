using Plots

points = [(10, 7), (13, 4), (11, 5), (8, 9)]

x_values = [point[1] for point in points]
y_values = [point[2] for point in points]

scatter(x_values, y_values, markershape=:circle, markercolor=:blue, markersize=8, label="")

labels = ["A", "B", "C", "D"]
for (i, (x, y)) in enumerate(points)
    annotate!(x, y + 0.5, text(labels[i], :left, 8))
end

xlabel!("f_1")
ylabel!("f_2")
title!("Criteria space")
