import uuid


class Entry:
    def __init__(self, text):
        self.text = text

    def get_normalize_form(self):
        text = self.text.replace(" ", "_")
        return text

    def get_sense(self):
        sense_id = str(uuid.uuid1())
        content = '<sense id="' + sense_id + '" order="1">\n' \
                  + '<grammatical-info value="Noun">\n' \
                  + '</grammatical-info>\n' \
                  + '<example>\n' \
                  + '<form lang="vi"><text>Cô</text></form>\n' \
                  + '<translation type="Free translation">\n' \
                  + '<form lang="vi"><text>abc</text></form>\n' \
                  + '</translation>\n' \
                  + '<translation type="Free translation">\n' \
                  + '<form lang="en"><text>def</text></form>\n' \
                  + '<form lang="vi"><text>abc</text></form>\n' \
                  + '</translation>\n' \
                  + '</example>\n' \
                  + '</sense>\n'
        return content

    def __str__(self):
        content = '\n'
        guid = str(uuid.uuid1())
        content += '<entry dateCreated="2021-03-09T14:44:31Z" ' \
                   + 'dateModified="2021-03-09T14:57:54Z" ' \
                   + 'id="' + self.get_normalize_form() + '_' + guid + '" ' \
                   + 'guid="' + guid + '">\n' \
                   + '<lexical-unit>\n' \
                   + '<form lang="vi"><text>' + self.text + '</text></form>\n' \
                   + '</lexical-unit>\n' \
                   + '<trait name="morph-type" value="stem"/>\n' \
                   + self.get_sense() \
                   + '</entry>'
        return content


class Dict:
    def __init__(self):
        pass

    def __str__(self):
        with open("../tmp/template/dict.lift.template") as f:
            lines_template = f.read().splitlines()
        entry = Entry(text='em')
        content = '\n'.join(lines_template[:88]) + str(entry) + '\n' + lines_template[88]
        return content


dict = Dict()
with open("../tmp/dict/dict.lift", 'w') as f:
    f.write(str(dict))

with open("../tmp/template/dict.lift-ranges.template") as f:
    template = f.read().splitlines()
with open("../tmp/dict/dict.lift-ranges.lift", 'w') as f:
    f.write(template[0])
