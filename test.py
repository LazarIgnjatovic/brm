import pandas as pd
import numpy as np
import tensorflow as tf
import logging

logging.basicConfig(level=logging.INFO)
logging.info('Loading model...')
model = tf.keras.models.load_model('/app/model')

# Load the test data
logging.info('Loading test data...')
test_data = pd.read_csv('/app/test/testset.csv')
logging.info('Data loading done.')

# Perform testing and print the results
logging.info('Performing testing...')
for data in test_data:
    test=data.drop([x for x in data.columns if 'Label_' in x], axis=1)
    results = model.predict(test.to_numpy())
    print(results)

input('Press any key to continue...')
