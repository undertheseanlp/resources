# Phân tích BKT

Với Treebank BKT

Sinh ra file stats.xml

```
perl tools/conllu-stats.pl UD_Vietnamese-BKT2/*.conllu > bkt2_docs/stats.xml 
```

```
perl tools/conllu-stats.pl --oformat newdetailed --release 2.6 --treebank UD_Vietnamese-BKT2 --docs bkt2_docs --data . --lang vi 
```


Với Treebank BKT

Sinh ra file stats.xml

```
cd tmp
perl ../extras/tools/conllu-stats.pl UD_Vietnamese-BKT2/*.conllu > bkt_docs/stats.xml 
```

Sinh ra docs theo format `newdetailed`

```
cd tmp
export BKT_DOCS=btk_docs
rm -rf $BKT_DOCS/treebanks/*
perl ../extras/tools/conllu-stats.pl --oformat newdetailed --release 2.6 --treebank UD_Vietnamese-BKT2 --docs bkt_docs --data . --lang vi
```


So sánh 2 treebank 

```
cd tmp
perl tools/conllu-stats.pl --oformat hubcompare UD_Vietnamese-BKT UD_Vietnamese-VTB  > comparison.md 
```

Với BKT Treebank 

```
cd tmp
python ../extras/tools/validate.py --lang=vi UD_Vietnamese-BKT2/*.conllu
```