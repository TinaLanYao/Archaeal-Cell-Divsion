#!/bin/bash
#call on bashrc to use aliases
#shopt -s expand_aliases
#source ~/.bashrc


for i in `seq 6 1 6`; do
for j in `seq 15 5 15`; do
for k in `seq 1 1 10`; do
	cp -R ./analyse_all/* ./SIGMA=${i}_PACK=${j}_SEED=${k}/
	cd ./SIGMA=${i}_PACK=${j}_SEED=${k}/
	#rm circle_fit_mem.dat
	python3 cyto.py
	#plot cell division radius
	sh circle_fit_mem.sh
	# plot long cell radius
	python3 long_measure.py
	python3 divisionsuccess.py ${i} ${j} ${k}
	cd ..
done
done
done

for i in `seq 5 1 8`; do
for j in `seq 10 5 40`; do
	python3 averageradius.py ${i} ${j}
done
done
python3 averagesuccess.py
