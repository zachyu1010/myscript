set height unlimited

b KneronResizeOperator<int>::KneronResizeBilinear
b KL530Operator.cpp:2271 if c == 0 && w == 0
commands
silent
printf "%d. ", h
set $outSum = ((1 << 6) - weight) * input_left_value + weight * input_right_value
printf "%dx%d + %dx%d = %d, %d\n", input_left_value, ((1 << 6) - weight), input_right_value, weight, $outSum, $outSum << 10
continue
end

b KneronResizeOperator<int>::KneronResizeNearest
b KL530Operator.cpp:2127 if c == 0 && w == 14
commands
silent
printf "%d. ", h
printf "%d, %d, %d, %d\n", output_value, h_weight[h], x.get(), in_h[h]
continue
end