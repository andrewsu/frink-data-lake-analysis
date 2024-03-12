#!/usr/bin/sh

mkdir output

# dream-kg
gawk '$2=="<http://schema.org/name>"' lakefs/dream-kg/main/dreamkg-prov.ttl | 
	sed 's/.*name> "//;s/" .*//' > output/dream-kg-names.txt
python3 query_wikidata.py output/dream-kg-names.txt > output/dream-kg-names.WD.txt

# scales
