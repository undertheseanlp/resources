# Bài toán tokenize và tách từ

Nhãn UD dựa trên quan điểm **từ vựng** về *ngữ pháp*, có nghĩa là các quan hệ thuộc dựa trên các **từ**. Do đó, các đặc điểm hình vị được coi như là một đặc tính của từ và không cố gắng chia từ thành các từ tố.
Tuy nhiên, điều quan trọng cần lưu ý rằng đơn vị cơ bản của việc gán nhãn là các *từ cú pháp* không phải là *từ phiên âm* hoặc *chữ viết*), có nghĩa là chúng tôi muốn tách ra một cách có hệ thống các clitics, như trong tiếng Tây Ban Nha *dámelo = da me lo*, tách ra các từ rút gọn, như trong tiếng Pháp *au = à le*. Chúng tôi coi những trường hợp này như các trường hợp *token chứa nhiều từ* vì một chữ tương đương với nhiều từ (cú pháp).
Trong một số trường hợp ngoại lệ khác, có thể cần phải đi theo hướng ngược lại, kết hợp một số chữ thành một từ. Bắt đầu từ phiên bản v2 của chỉ dẫn UD, những *từ nhiều token* được chấp nhận đối với một số trường hợp cụ thể, như số *20 000* hay các từ viết tắt *e. g.,* miễn là những hiện tượng này được chấp thuận và quy định rõ ràng trong những tài liệu dành riêng cho từng ngôn ngữ.
Chú ý rằng, kỹ thuật này không nên bị lạm dụng cho những cụm từ như *in spite of* hay *by and large*, nên được gán thành các nhãn quan hệ chuyên dụng.

Vì bài toán tách từ là một nhiệm vụ không đơn giản trong nhiều ngôn ngữ, và vì tính hiệu quả của việc huấn luyện dữ liệu treebank phụ thuộc khá nhiều vào việc tách từ đối với dữ liệu mới, điều quan trọng là cần tài liệu hóa những nguyên tắc tách từ cho mỗi ngôn ngữ. Bản chất của tài liệu này sẽ chuyên biệt cho từng ngôn ngữ, thể hiện đặc điểm và hệ thống chữ viết của ngôn ngữ.

Chú thích:

* Tiếng Tây Ban Nha *dámelo = đưa nó cho tôi, da = cho, me = tôi, lo = nó*

Tham khảo:

* (1): https://universaldependencies.org/u/overview/tokenization.html
