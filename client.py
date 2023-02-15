import pandas as pd
import requests

chunk_size = 1000
data_chunks = pd.read_csv('/home/kali/brm/data/test/testset.csv',chunksize=chunk_size)

for i, chunk in enumerate(data_chunks):
    print(f"Sending request for chunk {i+1}...")
    test=chunk.drop([x for x in chunk.columns if 'Label_' in x], axis=1)
    json_data = test.to_json(orient='values')
    response = requests.post("http://localhost:8000/test", json=json_data)
    print(response.text)
    break