set height unlimited

set $mMacCnt = -1

set $mMacSt = 1
set $mMacEnd = 1
set $mCoreId = 0
set $mOchGrp = 0
set $mOch = 0
set $mRf = 0
set $mC = 0


b KLConvMAC::run
commands
silent
set $mMacCnt = $mMacCnt + 1
continue
end

b kl_out_conv_store.cpp:403

#KLConvMAC::DoBunchConv1x1
b kl_eu_conv_mac.cpp:3012 if ($mMacSt <= $mMacCnt && $mMacCnt <= $mMacEnd) && id == $mCoreId && ochGrp == $mOchGrp && och == $mOch && rf == $mRf && c == $mC
commands
silent
printf "========================================== (%d, %d: %d, %d, %d)\n", $mMacCnt, id, ochGrp, rf, c
printf "%dx%d=%d\n", mac_a1, mac_b1, mac_r1
continue
end


#KLConvMAC::DoBunchConv3x3DW
b kl_eu_conv_mac.cpp:3420 if ($mMacSt <= $mMacCnt && $mMacCnt <= $mMacEnd) && id == $mCoreId && ochGrp == $mOchGrp && och == $mOch && rf == $mRf && c == $mC
commands
silent
printf "========================================== (%d, %d: %d, %d, %d)\n", $mMacCnt, id, ochGrp, rf, c
printf "%dx%d=%d\n", mac_a1, mac_b1, mac_r1
printf "%dx%d=%d\n", mac_a2, mac_b2, mac_r2
printf "%dx%d=%d\n", mac_a3, mac_b3, mac_r3
printf "%dx%d=%d\n", mac_a4, mac_b4, mac_r4
printf "%dx%d=%d\n", mac_a5, mac_b5, mac_r5
printf "%dx%d=%d\n", mac_a6, mac_b6, mac_r6
printf "%dx%d=%d\n", mac_a7, mac_b7, mac_r7
printf "%dx%d=%d\n", mac_a8, mac_b8, mac_r8
printf "%dx%d=%d\n", mac_a9, mac_b9, mac_r9
continue
end
