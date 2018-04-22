#!/bin/bash

# split the files into training and testing
if [ $# -ne 1 ]; then
    echo 1>&2 Usage: [random seed]
    echo "e.g.405409"
    exit -1
fi



get_seeded_random()
{
  seed="$1"
  openssl enc -aes-256-ctr -pass pass:"$seed" -nosalt \
    </dev/zero 2>/dev/null
}

rm -rf test train
mkdir -p train/pos train/neg test/pos test/neg
cp -r txt_sentoken wholedata
cd wholedata/pos
ls |sort -R --random-source=<(get_seeded_random $1 ) |head -200 |xargs -I {} mv {} ../../test/pos
mv *  ../../train/pos
cd ../neg
ls |sort -R --random-source=<(get_seeded_random $1 ) |head -200 |xargs -I {} mv {} ../../test/neg
mv *  ../../train/neg
cd ../..
rm -rf wholedata
