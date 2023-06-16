#!/bin/bash

#values=(8 16 32 48 64)
values=(8 16 32 48 64)

for val in "${values[@]}"
do
	sed -i "s/#define NLOOP [0-9]\+/#define NLOOP $val/" stream_mpi.c 
	git add .
	git commit -m "auto update nloop"
	git push
	docker build . --tag=raijenki/mpik8s:smpi --no-cache
	docker push raijenki/mpik8s:smpi
	for i in 1 2 3
	do
		echo "STARTING $val - Trial $i" >> parint_4ranks.txt 
		kubectl create -f smpi-vanilla.yaml
		sleep 900
		kubectl describe job.batch.volcano.sh >> parint_4ranks.txt 
		kubectl delete -f smpi-vanilla.yaml
		sleep 10
		echo "FINISHED" >> parint_4ranks.txt
	done
done
