#!/bin/bash

# split the files into training and testing
rm -rf test train
mkdir -p train/pos train/neg test/pos test/neg
cp -r txt_sentoken wholedata
cd wholedata/pos
ls  |head -200 |xargs -I {} mv {} ../../test/pos
mv *  ../../train/pos
cd ../neg
ls  |head -200 |xargs -I {} mv {} ../../test/neg
mv *  ../../train/neg
cd ../..
rm -rf wholedata