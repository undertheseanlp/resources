# Phân tích VTB

Sinh ra doc 

```
cd extras
rm -rf ../tmp/vtb_docs/treebanks/*
 perl tools/conllu-stats.pl --oformat newdetailed --release 2.6 --treebank UD_Vietnamese-VTB  --docs ../tmp/vtb_docs --data . --lang vi
```

Bước 2: Kiểm tra TreeBank


```
python tools/validate.py --lang=vi VTB/vi_vtb-ud-train.conllu
```