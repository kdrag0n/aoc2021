#!/usr/bin/env bash

for i in $(seq 1 25); do
    cp 00_template/template.py day$i.py
    chmod +x day$i.py
done
