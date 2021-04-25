# read JSON file from Parser D:\DataTensor\*.txt
import ast
import glob
import json

# read file
# path = 'D:\DataTensor\*.txt'
path = r"/Users/matejpancak/PycharmProjects/new_project_test/Tensor1.txt"
files = glob.glob(path)
respond = {}
for file in files:
    with open(file, 'r') as f:
        response = json.dumps(f.read())
        response = ast.literal_eval(json.loads(response))
        for i in range(1, len(response)):
            idct = {}
            idct[i] = response[i]
            print(idct)

print(respond)
# example of imports to pandas DataFrame
# dataset = pandas.DataFrame.from_dict(respond, orient='index',
#                                    columns=['PLOAMdownstream', 'BIP', 'Psync', 'Plend', 'Identification', 'Bwmap'])
# example of table view
# from tabulate import tabulate
# print(tabulate(dataset, headers='keys', tablefmt='psql'))

# example of reading values from pandas
# bips = dataset['BIP'].value_counts(dropna=False)
# ploam_message = dataset['PLOAMdownstream'][1]['MessageID']

# example of converting pandas to json
# pandaBipJson = pandas.DataFrame.to_json(bips)
# print(pandaBipJson)
# print(ploam_message)
