import stanza

stanza.download('vi')
nlp = stanza.Pipeline('vi')

doc = nlp("Tuyến metro số 1 đang tăng tốc với việc các chuyên gia nước ngoài được cho phép vào Việt Nam để làm việc tại đây.")

print(doc.sentences[0].print_dependencies())