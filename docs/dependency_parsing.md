# Dependency Parsing

* `cmpobj`: Quan hệ so sánh

### Xây dựng Treebank chuẩn CoNLLU

Các bước xây dựng treebank chuẩn CoNLLU (1)

Bước 1: Thống kê Treebank

```
perl tools/conllu-stats.pl TREE_BANK/*.conllu > stats.xml 
```

Với Treebank BKT2 

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
perl tools/conllu-stats.pl UD_Vietnamese-BKT/*.conllu > bkt_docs/stats.xml 
```

Sinh ra docs theo format `newdetailed`

```
cd tmp
perl tools/conllu-stats.pl --oformat newdetailed --release 2.6 --treebank UD_Vietnamese-BKT --docs bkt_docs --data . --lang vi
```

So sánh 2 treebank 

```
cd tmp
perl tools/conllu-stats.pl --oformat hubcompare UD_Vietnamese-BKT UD_Vietnamese-VTB  > comparison.md 
```


Bước 2: Kiểm tra TreeBank


```
python tools/validate.py --lang=vi VTB/vi_vtb-ud-train.conllu
```

Với BKT Treebank 

```
cd tmp
python tools/validate.py --lang=vi UD_Vietnamese-BKT/*.conllu 
```
  


Tham khảo

(1): https://universaldependencies.org/release_checklist.html