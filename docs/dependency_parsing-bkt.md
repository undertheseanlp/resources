# Phân tích BKT

Sinh ra docs theo format `newdetailed`

```
cd tmp
rm -rf bkt_docs/treebanks/*
perl ../extras/tools/conllu-stats.pl --oformat newdetailed --release 2.6 --treebank UD_Vietnamese-BKT2 --docs bkt_docs --data . --lang vi
```

Validate TreeBank

```
cd tmp
python ../extras/tools/validate.py --lang=vi UD_Vietnamese-BKT2/*.conllu
```

Sinh ra file stats.xml

```
cd tmp
perl ../extras/tools/conllu-stats.pl UD_Vietnamese-BKT2/*.conllu > bkt_docs/stats.xml 
```

So sánh 2 treebank 

```
cd tmp
perl tools/conllu-stats.pl --oformat hubcompare UD_Vietnamese-BKT UD_Vietnamese-VTB  > comparison.md 
```

