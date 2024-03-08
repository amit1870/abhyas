from pathlib import Path

import readwrite as fdr

BASE_DIR = Path(__file__).resolve().parent
WORK_DIR = BASE_DIR / 'workspc'
FILE_PATH = WORK_DIR / 'BIGFILE.txt'
CSV_PATH = WORK_DIR / 'BIGFILE.csv'
SML_FILE_PATH = WORK_DIR / 'SMLFILE.txt'
CSV_FILE_PATH = WORK_DIR / 'SMLFILE.csv'

word = 'sitaram'
rplword = 'radhakrishna'

# replaced = fdr.replace_word_in_iterator(FILE_PATH, word, rplword)
# print(replaced)

csv_dict = fdr.csv_to_dict(CSV_PATH)
# print(csv_dict)

CSV_PATH = fdr.dict_to_csv(csv_dict, CSV_PATH)
print(CSV_PATH)


