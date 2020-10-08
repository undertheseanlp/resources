# Dependency Parsing

* `cmpobj`: Quan hệ so sánh

### Xây dựng Treebank chuẩn CoNLLU

Các bước xây dựng treebank chuẩn CoNLLU (1)

Bước 1: Thống kê Treebank

```
perl tools/conllu-stats.pl TREE_BANK/*.conllu > stats.xml 
```

Bước 2: Kiểm tra Treebank

```
python tools/validate.py --lang=vi VTB/vi_vtb-ud-train.conllu 
```



Tham khảo

* (1): https://universaldependencies.org/release_checklist.html
* (2): https://universaldependencies.org/u/dep/index.html
