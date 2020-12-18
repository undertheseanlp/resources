# Dependency Parsing

Phân tích cú pháp phụ thuộc

Không phân tích chủ nghữ, vị ngữ, các cụm danh từ, động từ... thay vì đó, phân tích quan hệ phụ thuộc giữa các từ trong
câu với nhau.

**Quan hệ phụ thuộc** 

Một quan hệ phụ thuộc thể hiện bằng một mũi tên có hướng, trong đó

* Phần đầu gọi là head (governor, regent)
* Phần mũi tên là dependent (modifer, subordinate,...)
* Nhãn phụ thuộc tương ứng giữa hai từ

**Nhập nhằng quan hệ phụ thuộc**

Xét câu sau:

```
Các nhà khoa học đếm cá voi từ không gian
```

Có 2 cách hiểu: cách hiểu đầu tiên là "từ không gian, các nhà khoa học đếm cá voi (dưới đại dương)", cách hiểu thứ hai là
"các nhà khoa học đếm những con cá voi từ không gian đến"

Cách hiểu đầu tiên chính xác và khả thi hơn. Để biết được điều này, ta cần biết được cụm từ `từ không gian` nên bổ nghĩa 
cho động từ `đếm` thay vì cụm từ `cá voi`.