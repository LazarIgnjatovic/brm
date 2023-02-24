import pandas as pd
import grequests
import logging
import time
import json
from statistics import mean
import numpy as np

test_url = "http://localhost:80/test"
testfile_path = './testset.csv'

logging.basicConfig(level=logging.INFO)

def read_chunks(path, chunk_size):
    data_chunks = pd.read_csv(path,chunksize=chunk_size)
    return data_chunks

def form_requests(chunks, url):
    requests=[]
    for i, chunk in enumerate(chunks):
        test = chunk.drop([x for x in chunk.columns if 'Label_' in x], axis=1)
        json_data = test.to_json(orient='values')
        requests.append(grequests.post(url, json=json_data))
    return requests

def run_requests(reqs,bl_size=50):
    results = []
    for resp in grequests.imap(reqs, size=bl_size):
        # results+=json.loads(resp.text)
        var = resp.text
    return results
def run_test(chunksizes: list, tests_num):
    results = pd.DataFrame(columns=["chunksize","loadtime","reqtime","exetime"])
    for ch_size in chunksizes:

        logging.info(f"testing for chunskize: {ch_size}")
        start_time = time.time()
        data = read_chunks(testfile_path, ch_size)
        load_time = time.time() - start_time
        logging.info(f"loadtime: {load_time}")

        start_time = time.time()
        reqs = form_requests(data,test_url)
        req_time = time.time() - start_time
        logging.info(f"request_time: {req_time}")

        test_times=[]
        for i in range(0, tests_num):
            logging.info(f"execution test {i} for chunskize: {ch_size}")
            start_time = time.time()
            run_requests(reqs)
            exe_time = time.time() - start_time
            test_times.append(exe_time)
        test_time=mean(test_times)

        logging.info(f"exe_time: {test_time}")

        results = results.append({
            "chunksize": ch_size,
            "loadtime": load_time,
            "reqtime": req_time, 
            "exetime": test_time
            }
            , ignore_index=True)
    return results

res = run_test([100000,500000,1000000],1)
res.head()