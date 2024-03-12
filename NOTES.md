## Dreamkg

ttl file, seems straightforward

```
$ wc *
  32460  141697 6069221 dreamkg-prov.ttl
   7821   43141 1307103 dreamkg.ttl
  40281  184838 7376324 total
```

## Pubmed-mimic

```
$ wc *
        0         1        27 entity_node.Header.csv
   250977    535997  13101974 entity_node.csv
        0         1        26 rela_node.Header.csv
 18352179  18352179 673678284 rela_node.csv
 18603156  18888178 686780311 total
```

Examine predicates: 

```
$ gawks '{print $3}' rela_node.csv | sort | uniq -c | sort -k1nr | more
2223662 LOCATION_OF
1758014 AFFECTS
1549159 TREATS
1544559 COEXISTS_WITH
1198144 INTERACTS_WITH
1031114 PROCESS_OF
 924094 CAUSES
 816950 PART_OF
 668853 ASSOCIATED_WITH
 537916 STIMULATES
 529827 INHIBITS
 487481 USES
 467851 AUGMENTS
 449816 DISRUPTS
 370807 compared_with
 335442 DIAGNOSES
 320163 PREDISPOSES
 301438 ISA
 258025 PRODUCES
 234354 ADMINISTERED_TO
 233021 PREVENTS
 232543 NEG_AFFECTS
```

Examine source DB:

```
$ gawks '{print $4}' rela_node.csv | sort | uniq -c | sort -k1nr | more
18017323 PubMed
 223121 MIMIC
 111615 MIMIC;PubMed
    120 MIMIC_SDoH
```

## Scales

Highly nested structure
Entities seem to be related to courts.ttl, judge_entities.ttl

```
<http://schemas.scales-okn.org/rdf/scales#JudgeEntity/SJ003188> scales:hasFJCNodeID 1.393806e+06 ;
    scales:hasJudgeEntityType "FJC Judge" ;
    scales:hasName "Susan Owens Hickey" .
```

Is ‘FJCNodeID 1.393806e+06’ some sort of external identifier?

‘Courts.ttl’ doesn’t appear to have any external identifier, but not that many (94)

## Semopenalex

Very small sample
Citation counts of publications? Topic categories?

## Urbanflooding

39_all was ~30 GB? I’m analyzing 1.6GB subset -- ~16 million rows

```
$ gawk '{print $2}' partial_39_all.nq | sort | uniq -c | sort -k1nr | more
5902076 <https://schema.org/identifier>
2951038 <https://schema.org/geo>
1475520 <https://schema.org/variableMeasured>
1472415 <https://schema.org/description>
1470613 <https://schema.org/additionalType>
1470612 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>
1470612 <https://schema.org/name>
```

Names are not helpful

```
<https://ufokn.org/id/urmi/dpq5b7xjedj2> <https://schema.org/name> "dpq5b7xjedj2" .
<https://ufokn.org/id/urmi/dpmh0qpbwvxu> <https://schema.org/name> "dpmh0qpbwvxu" .
<https://ufokn.org/id/urmi/dpkst5vdy01g> <https://schema.org/name> "dpkst5vdy01g" .
<https://ufokn.org/id/urmi/dpj10t25w9rd> <https://schema.org/name> "dpj10t25w9rd" .
<https://ufokn.org/id/urmi/dpjqbw3yprxd> <https://schema.org/name> "dpjqbw3yprxd" .
<https://ufokn.org/id/urmi/dngzxzthfwrr> <https://schema.org/name> "dngzxzthfwrr" .
<https://ufokn.org/id/urmi/dpjh2ctnstfh> <https://schema.org/name> "dpjh2ctnstfh" .
<https://ufokn.org/id/urmi/dpj50rcu8byu> <https://schema.org/name> "dpj50rcu8byu" .
```

Neither are variable measured

```
<https://ufokn.org/id/urmi/dngyy0u1z46b> <https://schema.org/variableMeasured> _:c60178c5516c8a7b20a11c57e0ab150f .
<https://ufokn.org/id/urmi/dngz5ftsf0y4> <https://schema.org/variableMeasured> _:a31ebdc88094fae6d3cf2bc7125de8a7 .
<https://ufokn.org/id/urmi/dpm5w1us3rp8> <https://schema.org/variableMeasured> _:3b5754acc19aebdb8e78c3b78aa3b2d .
<https://ufokn.org/id/urmi/dnvh7mbyyud2> <https://schema.org/variableMeasured> _:64a5030748ca53d1e3c10ee3c1434440 .
<https://ufokn.org/id/urmi/dpmgh2rknt6d> <https://schema.org/variableMeasured> _:832fc90cf9bac2253e5242b005746b9f .
<https://ufokn.org/id/urmi/dpkfmd7x9zbn> <https://schema.org/variableMeasured> _:d599d052532ca89fc4e9b17987b4848f .
<https://ufokn.org/id/urmi/dnum0mx6vu3d> <https://schema.org/variableMeasured> _:5f1d1a202f92386ef770cbe22c48a3d3 .
<https://ufokn.org/id/urmi/dph1d2s01u1f> <https://schema.org/variableMeasured> _:ff1017ba66ed39cf90f55579c0c516f2 .
```

