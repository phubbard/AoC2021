#!/bin/bash

echo "Building..."
gcc brad_p17.c -Ofast -fopenmp -o brad_p17.exe
echo "Running..."
./brad_p17.exe
echo "Done, no errors."



