# Phân tích VTB

Sinh ra doc 

```
cd tmp
rm -rf bkt_docs/treebanks
perl ../extras/tools/conllu-stats.pl --oformat newdetailed --release 2.6 --treebank UD_Vietnamese-BKT2 --docs bkt_docs --data . --lang vi
```

Bước 2: Kiểm tra TreeBank


```
python tools/validate.py --lang=vi VTB/vi_vtb-ud-train.conllu
```