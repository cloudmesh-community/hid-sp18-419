#!/bin/sh

file='configuration_gce_419.json'

if [ ! -f ~/.cloudmesh/${file} ]; then
   cp etc/${file} ~/.cloudmesh/
fi
