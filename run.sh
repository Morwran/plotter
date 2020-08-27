#!/bin/bash
qcustomplot_dir=$HOME"/prj/qcustomplot-python/"

if [ -d $qcustomplot_dir ];then 
	LD_LIBRARY_PATH=$qcustomplot_dir python plotter/plotter.py $qcustomplot_dir
fi

if ! [ -d $qcustomplot_dir ];then 
	echo "ERROR: Не найден путь к биндам qcustomplot";
fi	