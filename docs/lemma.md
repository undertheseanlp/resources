# Lemma

Trong xử lý ngôn ngữ tự nhiên, nhất là trong tiếng Anh, các token thường không ở dạng nguyên bản.

Ví dụ trong câu **"The boy's cars are different colors"**, các token `boy's`, `cars`, `different`, `colors` đều không ở dạng nguyên bản.

Dạng nguyên bản của `Boy's` là `boy`, `cars` là `car`, `different` là `differ`, `colors` là `color`.

Ở dạng nguyên bản, câu trên được viết lại như sau **"the boy car differ color"**

Có hai phương pháp thường được sử dụng để chuyển một token sang dạng nguyên bản là **Lemmatization** và **Stemming**
 
Kỹ thuật **Stemming** thường dùng một phương pháp heuristic (như loại bỏ hay thay thế một số hậu tố ở cuối từ). Như đối với trường hợp danh từ ở dạng số nhiều như `cars` và `colors`, đều có thể chuyển về dạng gốc bằng cách đơn giản bỏ thêm ký từ `s` ở cuối câu. 

Kỹ thuật **Lemmatization** thường sử dụng các kỹ thuật hơn, như phân tích hình thái của từ. Ví dụ như từ `saw`, stemming khó có thể giải quyết, trong khi với kỹ thuật Lemmatization có thể biết `saw` là dạng quá khứ của từ `see`, và chuyển `saw` về dạng nguyên bản `see`.

# Các vấn đề với nhãn lemma

- Xử lý thế nào với trường hợp viết tắt như TPHCM, HN, ĐN ?

Tham khảo

(1): (2018). Stemming and lemmatization. *Introduction to Information Retrieval*. https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html