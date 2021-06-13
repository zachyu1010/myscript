silent
printf "%d. %d, %d, %d, %d, %d\n", w, output_value.m_obj, input_left_value, ((1 << 6) - weight), input_right_value, weight
continue
end

silent
if ridx == 0 && didx == 0
printf "%d. %d, %d, %d, %d\n", cidx, i32LValue, lWeight, i32RValue, rWeight
end
continue
end

silent
if ridx == 0 && didx == 0
printf "%d. %d, %d, %d\n", cidx, i32LValue, i32RValue, a
end
continue

KLConvMAC::DoBunchHS() 
b /mnt/d/project/CSIMv2/kdp720_hw_csim_latest/src/kernels/kl_eu_conv_mac.cpp:3905
commands
        silent
        if rf == 0 && ochGrp == 0 && och == 0
          printf "%d. %d * %d + %d * %d = %d, %d\n", c, mac_a1, mac_b1, mac_a2, mac_b2, (mac_r1 + mac_r2) >> 6, fraction
        end
        continue
end

