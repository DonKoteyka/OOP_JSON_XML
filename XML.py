import xml.etree.ElementTree as ET
file_path = "1.xml"



# def read_json(file_path, word_max_len=6, top_words_amt=10):
#     dictionary = dict()
#     tree = ET.parse(file_path)
#     with open(file_path, 'r', encoding='utf-8') as f:
#         str_words = json.load(f)['rss']['channel']['items']
#     worlds =  list(filter(lambda x: len(x)>word_max_len, list(sum((map(lambda i: (i['description']).split(), str_words)), []))))
#     [dictionary.setdefault(i, worlds.count(i)) for i in worlds]
#     res = [i[0] for i in sorted(dictionary.items(),key=lambda i: i[1], reverse=True)[0:top_words_amt]]
#     return res
# for i in item:
#     a = i.find('description')
#     print(a.text)


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    dictionary = dict()
    description = list()
    tree = ET.parse(file_path)
    item = tree.findall('channel/item')
    for i in item:
        description.append((i.find('description').text).split())
    worlds = list(
        filter(lambda x: len(x) > word_max_len, list(sum(description, []))))
    [dictionary.setdefault(i, worlds.count(i)) for i in worlds]
    res = [i[0] for i in sorted(dictionary.items(),key=lambda i: i[1], reverse=True)[0:top_words_amt]]
    return res


print(read_xml(file_path))