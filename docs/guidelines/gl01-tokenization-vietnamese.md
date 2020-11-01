# Bài toán tokenize cho tiếng Việt

## Danh từ đơn vị, tách thành 2 token

1km² -> 1 km², 1kg -> 1 kg

## Email, Url: Không tách

abc@gmail.com, https://www.abc.com/index.php?def=123

## Số

Số âm: -123.34

Số với định dạng 123.456.789 

Phân số: 

- Trường hợp nhập nhằng 

Phân số và ngày tháng: 1/2 (một phần 2 hoặc ngày 1 tháng 2)

Số thứ tự ở đầu câu: không tách

* 1., 2. 
* a., b.

## Dấu gạch ngang (-) ở giữa

Đây là trường hợp khá phức tập

* 2010-2019: cần tách thành 2 token
* quan hệ `Moscow-Washington`: cần tách thành 2 token
* Trung tâm nhiệt đới `Việt-Nga`

Tên riêng: cần giữ nguyên

Ward-Warmedinger

Từ nước ngoài: giữ nguyên 

* e-learning, knowledge-based

Từ ghép: giữ nguyên

* chủ nghĩa `Mác-Lênin`
* lưới `ni-lông`
* QĐ-TTg

Tham khảo: 

* [Dấu gạch ngang và dấu gạch nối](https://baodanang.vn/channel/6059/201501/dau-gach-ngang-va-dau-gach-noi-2391622/)

# Dấu chấm (.) ở giữa từ

* Đề tài trọng điểm cấp nhà nước `KC.08.30`