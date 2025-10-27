set terminal pngcairo size 1200,600 font "Arial,12"
set output 'dope_profile_MT.png'

set title "DOPE Score Profile: Templates vs Best WT Model" font "Arial,14"
set xlabel "Residue Number" font "Arial,12"
set ylabel "DOPE Score" font "Arial,12"

set grid
set key top right font "Arial,10"

set style line 1 lt 1 lw 2 lc rgb "#E69F00" dt 2
set style line 2 lt 1 lw 2 lc rgb "#56B4E9" dt 2
set style line 3 lt 1 lw 2 lc rgb "#009E73" dt 2
set style line 4 lt 1 lw 3 lc rgb "#000000"

# Skip comment lines starting with #
set datafile commentschars "#"

# Plot using column 1 (residue number) and column 42 (TOTAL DOPE score)
plot 'dope_shope_6E07.profile' using 1:42 with lines ls 1 title "Template 1", \
     'dope_shope_6E08.profile' using 1:42 with lines ls 2 title "Template 2", \
     'dope_shope_7SNF.profile' using 1:42 with lines ls 3 title "Template 3", \
     'dope_shope_P11413M.profile' using 1:42 with lines ls 4 title "Best MT Model"