#!/usr/bin/sh

mkdir output

# dream-kg
gawk '$2=="<http://schema.org/name>"' lakefs/dream-kg/main/dreamkg-prov.ttl | 
	sed 's/.*name> "//;s/" .*//' > output/dream-kg-names.txt
python3 query_wikidata.py output/dream-kg-names.txt > output/dream-kg-names.WD.txt

# scales
grep 'hasName' lakefs/scales-kg/courts.ttl | 
	sed '
	s/.*hasName "/United States /;
	s/Court,/Court for the/;
	s/S\./Southern /;
	s/N\./Northern /;
	s/E\./Eastern /;
	s/W\./Western /;
	s/C\./Central /;
	s/M\./Middle /;
	s/D\./District of/;
	s/" .*//' > output/scales-kg-courts.txt
python3 query_wikidata.py output/scales-kg-courts.txt > output/scales-kg-courts.WD.txt

grep 'hasName' lakefs/scales-kg/judge_entities.ttl | 
	sed 's/.*hasName "//;s/".*//;s/\([A-Z]\) /\1. /' > output/scales-kg-judges.txt
python3 query_wikidata.py output/scales-kg-judges.txt > output/scales-kg-judges.WD.txt


# Summarize mapping stats
for file in output/*.WD.txt; do
    echo $file
    total_count=`gawkt '{print $1}' $file | sort -u | wc -l`
    no_mapping=`gawkt '$2=="None"{print $1}' $file | sort -u | wc -l`
    one_mapping=`gawkt '$2!="None"{print $1}' $file | sort | uniq -c | gawk '$1==1' | wc -l`
    multi_mapping=`gawkt '$2!="None"{print $1}' $file | sort | uniq -c | gawk '$1>1' | wc -l`
    echo -e "Unique entities:\t$total_count"
    echo -e "No Wikidata mapping:\t$no_mapping"
    echo -e "One Wikidata mapping:\t$one_mapping"
    echo -e "Many Wikidata mappings:\t$multi_mapping"
    echo ""
done
