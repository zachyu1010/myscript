set height unlimited

set $mConvCnt = -1

set $mConvSt = 0
set $mConvEnd = 0
set $mOch = 0
set $mR = 0
set $mC = 0


b KL530Operator.cpp:683
commands
silent
set $mConvCnt = $mConvCnt + 1
continue
end

#DoConvolution
b KL530Operator.cpp:863 if ($mConvSt <= $mConvCnt && $mConvCnt <= $mConvEnd) && och == $mOch && r == $mR && c == $mC
commands
silent
printf "========================================== (%d, -: %d, %d, %d)\n", $mConvCnt, och, r, c
continue
end

b KL530Operator.cpp:872 if ($mConvSt <= $mConvCnt && $mConvCnt <= $mConvEnd) && och == $mOch && r == $mR && c == $mC
commands
silent
printf "%dx%d=%d\n", data, weight, data * weight
continue
end
