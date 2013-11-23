#!/bin/sh
indexer delta --rotate
indexer --merge blog_index delta --merge-dst-range deleted 0 0 --rotate