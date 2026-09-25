#!/bin/bash
# Render every page's figures with the page checker, several pages at a time.
cd "$(dirname "$0")/.."
run() { PC_TAG=${TAG:-v9}$1 PYTHONIOENCODING=utf-8 python review/page_check.py $2 ${3}_BODY ${3}_NAV $1 > review/${TAG:-v9}check_$1.txt 2>&1; }
run p1 p1 P1 & run p2 p2 P2 & run p3 p3_sec P3 & run p4 p4_sec P4 & run p5 p5_sec P5 & run p6 p6 P6 & wait
run p6a p6a P6A & run p7 p7 P7 & run s1 s1 S1 & run s2 s2page S2 & run s3 s3 S3 & run s4 s4 S4 & wait
run g1 g1 G1 & run g2 g2 G2 & run g3 g3 G3 & run g5 g5 G5 & run g6 g6 G6 & run g7 g7 G7 & wait
run g8 g8 G8 & run gl gl GL & run ci ci CI & wait
echo all rendered
