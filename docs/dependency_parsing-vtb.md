# Phân tích VTB

Sinh ra docs theo format `newdetailed`

```
cd extras
rm -rf ../tmp/vtb_docs/treebanks/*
 perl tools/conllu-stats.pl --oformat newdetailed --release 2.6 --treebank UD_Vietnamese-VTB  --docs ../tmp/vtb_docs --data . --lang vi
```

Sinh ra lemma docs

```
source active resources 
cd extras/ud_analyze
python make_lemma_doc.py --treebank ../UD_Vietnamese-VTB/ --docs ../../tmp/vtb_docs/
```

Validate TreeBank


```
python tools/validate.py --lang=vi VTB/vi_vtb-ud-train.conllu
```