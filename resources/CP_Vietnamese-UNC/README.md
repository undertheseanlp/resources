# CP_Vietnamese-UNC

`Corpus` | `Vietnamese` | `Underthesea News Corpus`

Vietnamese News Corpus is a text corpus collected by `underthesea team` in 2020 - 2021 from [dantri](https://dantri.com.vn/) website.

We collect documents from 10 categories: business (kinh-doanh), education (giao-duc-huong-nghiep), entertainment (giai-tri), health (suc-khoe), science (khoa-hoc-cong-nghe), society (xa-hoi), sport (the-thao), tech (suc-manh-so), travel (du-lich), world (the-gioi).

This corpus contains more than 40,000 sentences from 2,600 documents.

### Statistics

```
Number of topics    : 10
Number of documents : 2653
Number of sentences : 41947 
```

Older Version

<table>
<tr>
  <th>Version</th>
  <th>Year</th>
  <th>Number of topics</th>
  <th>Number of documents</th>
  <th>Number of sentences</th>
</tr>
<tr>
  <td>1.0</td>
  <td>2021</td>
  <td>10</td>
  <td>200</td>
  <td>4613</td>
</tr>
</table>

### Data Format and Sample

Each document have metadata doc_id, url and date.

``` 
# doc_id = news_world_015
# url = https://dantri.com.vn/the-gioi/gan-100000-ca-covid-19-tai-my-chi-trong-1-ngay-anh-tai-phong-toa-ca-nuoc-20201101114516249.htm
# date = 20201101
Gần 100.000 ca Covid-19 tại Mỹ chỉ trong 1 ngày, Anh tái phong tỏa cả nước
Sau 8 tháng chiến đấu với đại dịch Covid-19, Mỹ ghi nhận kỷ lục gần 100.000 ca mắc mới chỉ trong 1 ngày. Tại Anh, Thủ tướng Johnson công bố lệnh tái phong tỏa toàn quốc khi số người mắc vượt 1 triệu.
Mỹ đang trải qua làn sóng Covid-19 thứ 3
Washington Post đưa tin, con số gần 100.000 ca Covid-19 mới chỉ trong 1 ngày thứ Sáu là mức kỷ lục toàn cầu.
Cụ thể, theo số liệu của Đại học Johns Hopkins, Mỹ ghi nhận 99.321 ca mắc và 1.030 người tử vong trong ngày 30/10.
Con số trên là mức tăng cao chưa từng có được ghi nhận trong một ngày tại Mỹ.
Điều này cho thấy tình hình dịch bệnh ở nước này không có bất kỳ dấu hiệu cải thiện nào.
Theo đài phát thanh NPR, nước Mỹ đang trải qua làn sóng Covid-19 thứ 3, được cho là sẽ vượt xa 2 làn sóng trước đó.
Các chuyên gia Mỹ từ lâu đã cảnh báo về về sự gia tăng mạnh các ca mắc do sự thay đổi mùa, khi vi rút lây lan mạnh trong thời tiết lạnh hơn.
Hơn 1.000 người cũng tử vong vì Covid-19 mỗi ngày trong 2 ngày 28 và 29/10, tăng 16% so với hai tuần trước đó.
Nước Mỹ - vùng dịch lớn nhất thế giới - cho tới nay đã ghi nhận 9,4 triệu ca Covid-19 và hơn 236.000 người tử vong vì dịch bệnh.
Châu Âu bước vào mùa đông u ám
```

### Maintain Scripts 

Build Corpus

```
$ python scripts/build.py

[+] BUILD SUCCESS

# CORPUS STATISTICS
Number of topics    : 10
Number of documents : 2653
Number of sentences : 41947
```

### Changelog

* [View Full Changelog](CHANGELOG.md)

