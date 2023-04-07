#!/bin/bash

for i in {1..23}
do
    convert "peng-$i.svg" -resize 1000x1000 "png/peng-$i.png"
done

