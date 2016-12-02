#!/bin/bash

for f in $(ls *.py -B)
do
    mv $f 0$f
done
