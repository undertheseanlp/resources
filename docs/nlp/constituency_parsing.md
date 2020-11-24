# Constituency Parsing

Phân tích cú pháp thành phần là một bài toán trong xử lý ngôn ngữ tự nhiên, giúp giải quyết vấn đề nhập nhằng cú pháp.

Xét câu sau `Hằng ngắm mưa trong công viên.`, sau khi đã phân tích từ loại, phân tích cú pháp thành phần giúp tách câu 
thành từng phần như sau: 

```
(S (NP (Np Hằng)
 (VP (V ngắm)
 (NP (NP (N mưa))
 (PP (E trong)
 (NP (N công viên)))))
 (. .)) 
```

trong đó:

* S: chủ ngữ của câu
* NP: cụm danh từ
* VP: cụm động từ
* PP: cụm giới từ

