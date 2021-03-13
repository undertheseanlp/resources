import uuid
import joblib


class Sense:
    def __init__(self, part_of_speech):
        self.part_of_speech = part_of_speech.capitalize()

    def __str__(self):
        sense_id = str(uuid.uuid1())
        content = '<sense id="' + sense_id + '" order="1">\n' \
                  + '<grammatical-info value="' + self.part_of_speech + '">\n' \
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


class Entry:
    def __init__(self, form):
        self.form = form
        self.senses = []

    def get_normalize_form(self):
        form = self.form.replace(" ", "_")
        return form

    def add_sense(self, s):
        self.senses.append(s)

    def __str__(self):
        content = '\n'
        guid = str(uuid.uuid1())
        content += '<entry dateCreated="2021-03-09T14:44:31Z" ' \
                   + 'dateModified="2021-03-09T14:57:54Z" ' \
                   + 'id="' + self.get_normalize_form() + '_' + guid + '" ' \
                   + 'guid="' + guid + '">\n' \
                   + '<lexical-unit>\n' \
                   + '<form lang="vi"><text>' + self.form + '</text></form>\n' \
                   + '</lexical-unit>\n' \
                   + '<trait name="morph-type" value="stem"/>\n'
        for sense in self.senses:
            content += str(sense)
        content += '</entry>'
        return content


class Dict:
    def __init__(self, entries=[]):
        self.entries = entries

    def save(self, filepath):
        # read template
        with open("../tmp/template/dict.lift.template") as f:
            lines_template = f.read().splitlines()

        # empty file
        with open(filepath, 'w') as f:
            f.write('')

        # start write content
        f = open(filepath, 'a')

        print('Start write to dict')
        content = '\n'.join(lines_template[:88])
        f.write(content)
        BUCK_WRITE = 300
        buck_count = 0
        content = ''
        for entry in self.entries:
            buck_count += 1
            content += str(entry) + '\n'
            if buck_count >= BUCK_WRITE:
                f.write(content)
                content = ''
                buck_count = 0
        f.write(lines_template[88])
        f.close()
        print('Finish writing')

    def add_entry(self, entry):
        self.entries.append(entry)

    def __str__(self):
        n_entries = len(self.entries)
        return f'Dictionary: {n_entries} entries'


dictionary_data = joblib.load("../datasets/DI_Vietnamese-UVD/UVD.bin")
dict = Dict()
for word in dictionary_data:
    print(word)
    entry = Entry(word)
    for def_list in dictionary_data[word]:
        pos = def_list['tag']
        for sense_data in def_list['defs']:
            sense = Sense(part_of_speech=pos)
            entry.add_sense(sense)
    dict.add_entry(entry)

dict.save("../tmp/dict/dict.lift")

with open("../tmp/template/dict.lift-ranges.template") as f:
    template = f.read().splitlines()
with open("../tmp/dict/dict.lift-ranges.lift", 'w') as f:
    f.write(template[0])
