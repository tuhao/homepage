#!/bin/sh
/usr/local/bin/indexer delta --rotate
/usr/local/bin/indexer --merge blog_index delta --merge-dst-range deleted 0 0 --rotate
