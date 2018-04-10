#!/bin/bash

# split the files into training and testing 
mkdir -p train/pos train/neg test/pos test/neg
cp -r txt_sentoken wholedata
cd wholedata/pos
ls  |sort -R|head -200 |xargs -I {} mv {} ../../test/pos
mv *  ../../train/pos
cd ../neg
ls  |sort -R|head -200 |xargs -I {} mv {} ../../test/neg
mv *  ../../train/neg
cd ../..
rm -rf wholedata