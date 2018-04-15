#!/bin/sh

file='configuration_gce_419.json'

if [ ! -d ~/.cloudmesh ]; then
   mkdir ~/.cloudmesh
fi

if [ ! -f ~/.cloudmesh/${file} ]; then
   cp etc/${file} ~/.cloudmesh/
fi
