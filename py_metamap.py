from pymetamap import MetaMap
from mytool import mmi_parser as mmip
mm = MetaMap.get_instance('/home/feng/public_mm/bin/metamap20')

sents2 = ['John had a huge heart attack and fever']
# sents = ['cold', "John had huge heart attack and fever"]
txt_file = "clinical_txt/2_modified.txt"

# read a file line by line to a List
def read_line(txt_file):
    sentences = list()
    with open(txt_file, 'r') as f:
        # i = index number, l = 讀出的某一行內容
        for i, l in enumerate(f):
            sentences.append(l)
        lines = i + 1
        return sentences, lines


sents, lines = read_line(txt_file)
index_list = range(1, lines+1)
# 將剛剛讀出的行內容List, 傳給 mm.extract_concepts 取出概念
concepts, error = mm.extract_concepts(
    sents, index_list, word_sense_disambiguation=True)
counter = 0
str = []
number_for_everyone = 0
# 每個 concept 都有的數值, 紀錄現在印到了哪個 index
# 每個 index 只會印一次
whether_print = True
# 如果印出了 index 就不要印了 設為否
for concept in concepts:
    '''
    Concept : 
    Index 儲存行的資訊
    semtype 儲存 semantic type 的資訊
    '''    
    if number_for_everyone != int(concept.index) :
        whether_print = True
        number_for_everyone += 1 
    if concept.semtypes == "[clnd]" or concept.semtypes == "[dsyn]" :
        if whether_print:
            print("Index:"+concept.index)
            whether_print =False
        
        print("CUI:"+concept.cui, "SMT:"+concept.semtypes, "POS:"+concept.pos_info, 
        "PREFER_N:"+concept.preferred_name, "NEGATED:"+mmip.trigger_parser(concept.trigger)[5], "TRIGGER:"+concept.trigger)
        counter += 1
print(counter)
# Output format is : index, mm, score, preferred_name, cui, semtype, trigger, location, pos_info, tree_nodes
