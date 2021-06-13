#dumpIntSeqRange: print a range of CHxROWxCOL feature map.
define dumpIntSeqRange
    set $filename = $arg0
    set $addr = $arg1
    set $ch = $arg2
    set $r = $arg3
    set $c = $arg4
    set $chs = $arg5
    set $che = $arg6
    set $rs = $arg7
    set $re = $arg8
    set $cs_ = $arg9
    set $ce = $arg10
	
    set logging off
    eval "set logging file %s", $filename
    set logging redirect on
    set pagination off
    set logging on
	
    set $psrcnt = 0
    set $chi = $chs	
    while ($chi < $che)
            set $ri = $rs
            while ($ri < $re)
                    set $ci = $cs_
                    while ($ci < $ce)
                            printf "%d\n", ((int *)$addr)[$chi*$r*$c + $ri*$c + $ci]
                            set $ci = $ci + 1
                            set $psrcnt = $psrcnt + 1
                    end
                    set $ri = $ri + 1
            end
            set $chi = $chi + 1
    end

    set logging off
    set pagination on
    set logging redirect off
    set logging file gdb.txt
end
	
#dumpIntSeq: print number of the float value specified by length. 
define dumpFloatSeq
    set $filename = $arg0
    set $addr = $arg1
    set $len = $arg2

    set logging off
    eval "set logging file %s", $filename
    set logging redirect on
    set pagination off
    set logging on
    
    set $idx = 0	
    while ($idx < $len)
        printf "%f\n", ((float *)$addr)[$idx++]
    end

    set logging off
    set pagination on
    set logging redirect off
    set logging file gdb.txt
end

#dumpIntSeq: print number of the integer value specified by length. 
define dumpIntSeq
    set $filename = $arg0
    set $addr = $arg1
    set $len = $arg2

    set logging off
    eval "set logging file %s", $filename
    set logging redirect on
    set pagination off
    set logging on
    
    set $idx = 0	
    while ($idx < $len)
        printf "%d\n", ((int *)$addr)[$idx++]
    end

    set logging off
    set pagination on
    set logging redirect off
    set logging file gdb.txt
end
