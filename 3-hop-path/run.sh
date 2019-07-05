#!/bin/bash
simulaqron start --force --nodes Alice,Bob,Charlie --topology path
python alice.py &
alice_pid=$!
python bob.py &
bob_pid=$!
python charlie.py &
charlie_pid=$!
wait $alice_pid
wait $bob_pid
wait $charlie_pid
simulaqron stop