#!/bin/sh

#initialization
#mkdir -p /usr/local/etc/log
#mkdir -p /usr/local/etc/data/blog_index
#mkdir -p /usr/local/etc/data/delta
#indexer blog_index
#indexer delta

#update index
indexer delta --rotate
indexer --merge blog_index delta --merge-dst-range deleted 0 0 --rotate
