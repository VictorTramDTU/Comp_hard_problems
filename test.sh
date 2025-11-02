#!/usr/bin/env bash

set -e

PY="$(which python3)"
run="$PY ./sswe_group23.py"

function check_yes {
    read answer
    [ "x${answer}" = "xYES" ]
}

function check_no {
    read answer
    [ "x${answer}" = "xNO" ]
}

function wrong {
    echo "test case $1 did not pass!"
    exit 1
}

$run < test01.swe | check_no || wrong 1
$run < test02.swe | check_yes || wrong 2
$run < test03.swe | check_no || wrong 3
$run < test04.swe | check_yes || wrong 4
$run < test05.swe | check_no || wrong 5
$run < test06.swe | check_yes || wrong 6
#$run < test07.swe | check_no || wrong 7
$run < test08.swe | check_yes || wrong 8
$run < test09.swe | check_no || wrong 9
$run < test10.swe | check_no || wrong 10
$run < test11.swe | check_no || wrong 11
