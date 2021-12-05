#!/usr/bin/env bash

set -eufo pipefail

cd "$(dirname "$0")"

num="$(echo "$1" | tr -d 't')"
problem="${2:-}"

mkdir -p in
mkdir -p samples

if [[ ! -f in/$num ]]; then
    echo "Download input"
    curl -H "Cookie: session=$(cat .token)" "https://adventofcode.com/2021/day/$num/input" | tee in/$num
fi

touch samples/$num

if [[ -z "$problem" ]]; then
    ./day$num.py in/$num
else
    ./day${num}-2.py in/$num
fi
