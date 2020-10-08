# Vietnamese NLP Resources

Dự án xây dựng tài nguyên cho các bài toán NLP tiếng Việt  (wikipedia/open data cho NLP tiếng Việt)

## Ý tưởng 

* Cập nhật dữ liệu HÀNG TUẦN
* Tập trung vào bài toán Dependency Parsing
* Cập nhật dữ liệu từ wikipedia, baomoi
* Cho mô hình chạy gán nhãn tự động các câu thú vị nhất  
* Ít nhất 3 người gán nhãn lại 
* Ít nhất 3 người reviews 
* Tất cả qua giao diện text 
* Luồng phát triển qua git
* Chương trình hoàn toàn tự động thông qua các bot 

## Mô hình cải tiến

```
+----------------+    +----------------+     +----------------+
|                |    |                |     |                |
|    Đề Xuất     + -> |    Xem Xét     +  -> |   Cập Nhật     +
|                |    |                |     |                |
+-------+--------+    +-------+--------+     +-------+--------+
```

* Bước 1: Đưa các các đề xuất
* Bước 2: Các đề xuất được xem xét 
* Bước 3: Các đề xuất đúng sau khi được xem xét sẽ được cập nhật vào dữ liệu

**Câu hỏi 1**: Làm sao các mô hình luôn cải tiến chất lượng

- Cần chạy mô hình liên tục
- Cần có người để sửa sai cho mô hình
- Sau đó cập nhật lại mô hình với dữ liệu đã sửa sai 

## Lịch sử phiên bản

* (v0.2 - 20201003): Thêm idea tập trung vào bài toán dependency parsing
* (v0.1 - 20190720): Ý tưởng về nguồn tài nguyên mở cho các bài toán NLP tiếng Việt, nơi dữ liệu NLP tiếng Việt được mở cho tất
cả mọi người.



