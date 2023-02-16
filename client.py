import pandas as pd
import grequests
import json
import logging

test_url = "http://localhost:8000/test"
testfile_path = '/home/kali/RUO/data/test/testset.csv'
chunk_size = 10000
data_chunks = pd.read_csv(testfile_path,chunksize=chunk_size)
logging.basicConfig(level=logging.INFO)

#NOTE: Model has to be present inside of the docker volume used by containers

requests=[]
for i, chunk in enumerate(data_chunks):
    logging.info(f"Forming request for chunk {i+1}...")
    test = chunk.drop([x for x in chunk.columns if 'Label_' in x], axis=1)
    json_data = test.to_json(orient='values')
    requests.append(grequests.post(test_url, json=json_data))
    if i>20:
        break

for resp in grequests.imap(requests, size=10):
    logging.info(resp)
