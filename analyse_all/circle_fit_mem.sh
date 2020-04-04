#!/bin/bash
#$ -cwd

python3 cyto.py
g++ circle_fit_mem.cpp -o circle_fit_mem
./circle_fit_mem

gnuplot << EOT
set terminal pngcairo enhanced color font "Utopia,16" size 25cm,20cm linewidth 2

set xlabel "time"
set ylabel "radius" rotate by 90
set yrange [0:60]
set output 'radius_vs_time_mem.png'
plot 'circle_fit_mem.dat' u 1:4:5 with errorbars notitle

set xlabel "time"
set ylabel "diameter" rotate by 90
set yrange [0:120]
set output 'diameter_vs_time_mem.png'
plot 'circle_fit_mem.dat' u 1:6 notitle

exit
EOT
