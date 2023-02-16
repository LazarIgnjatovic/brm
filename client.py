import pandas as pd
import grequests
import json

chunk_size = 10000
data_chunks = pd.read_csv('/home/kali/brm/data/test/testset.csv',chunksize=chunk_size)

requests=[]
for i, chunk in enumerate(data_chunks):
    print(f"Sending request for chunk {i+1}...")
    test = chunk.drop([x for x in chunk.columns if 'Label_' in x], axis=1)
    json_data = test.to_json(orient='values')
    requests.append(grequests.post("http://localhost:8000/test", json=json_data))
    if i>2:
        break

for resp in grequests.imap(requests, size=10):
    print(resp)
