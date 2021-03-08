define printSeqRange
	set $ch = $arg0
	set $r = $arg1
	set $c = $arg2
	set $chs = $arg3
	set $che = $arg4
	set $rs = $arg5
	set $re = $arg6
	set $cs_ = $arg7
	set $ce = $arg8
	
	printf "%d, %d, %d, %d, %d, %d, %d, %d, %d\n", $ch, $r, $c, $chs, $che, $rs, $re, $cs_, $ce
	printf "*** print start\n"
	
	set $psrcnt = 0
	set $chi = $chs	
	while ($chi < $che)
		set $ri = $rs
		while ($ri < $re)
			set $ci = $cs_
			while ($ci < $ce)
				printf "%d\n", (*$seq)[$chi*$r*$c + $ri*$c + $ci]
				set $ci = $ci + 1
				set $psrcnt = $psrcnt + 1
			end
			set $ri = $ri + 1
		end
		set $chi = $chi + 1
	end
	printf "\n**** print end\n"
end
	