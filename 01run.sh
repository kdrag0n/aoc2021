#!/usr/bin/env bash

set -eufo pipefail

cd "$(dirname "$0")"

num="$(echo "$1" | tr -d 't')"
problem="${2:-1}"

mkdir -p in
mkdir -p samples

if [[ ! -f in/$num ]]; then
    echo "Download input"
    curl -H "Cookie: session=$(cat .token)" "https://adventofcode.com/2021/day/$num/input" | tee in/$num
fi

if [[ "$(cat in/$num)" == "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available." ]]; then
    rm -f in/$num
    exit
fi

if [[ ! -f samples/$num ]]; then
    touch samples/$num
    code samples/$num
fi

if diff -q day$num.py 00_template/template.py > /dev/null; then
    code day$num.py
fi

in_dir=in
if [[ "${3:-}" == "s"* ]]; then
    in_dir=samples
fi

if [[ "$problem" == "1" ]]; then
    pypy3 day$num.py $in_dir/$num
else
    pypy3 day${num}-2.py $in_dir/$num
fi
