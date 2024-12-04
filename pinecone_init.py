import os
import openai
from pinecone import Pinecone, ServerlessSpec,Index
from datetime import datetime
import time

openai.api_key = os.getenv('OPENAI_KEY')
pc = Pinecone(api_key=os.getenv('PINECONE_KEY'))

current_time = datetime.now().strftime('%Y%m%d%H%M%S%f')

index_name = "test-feedback-1024"

index = pc.Index(index_name)

# List of vector IDs to fetch
vector_ids = ['20241204003624614227_1', '20241204003624614227_2']

# Fetch vectors
response = index.fetch(ids=vector_ids, namespace='ns1')

print(response)

# Create index
# pc.create_index(
#     name=index_name,
#     dimension=1024,
#     metric="cosine",
#     spec=ServerlessSpec(
#         cloud="aws",
#         region="us-east-1"
#     ) 
# )
# print(f"Index created successfully!")

# # Data and embeddings
# data = [
#     {
#         "input": "test input", 
#         "output": "test output",
#         "feedback": "good"
#      },
#      {
#         "input": "test input", 
#         "output": "test output",
#         "feedback": "bad, overlap between steps"
#      }
# ]

# # Assign unique 'id' to each dictionary
# for idx, item in enumerate(data, start=1):
#     # Generate current datetime string
#     current_time = datetime.now().strftime('%Y%m%d%H%M%S%f')
#     # Combine datetime string with index to ensure uniqueness
#     item['id'] = f'{current_time}_{idx}'

# texts = [
#     f"Input: {item['input']} Output: {item['output']} Feedback: {item['feedback']}"
#     for item in data
# ]

# embeddings = pc.inference.embed(
#     model="multilingual-e5-large",
#     inputs=texts,
#     parameters={"input_type": "query"}
# )
# print(embeddings[0])

# # Insert data and embeddings
# # Wait for the index to be ready
# while not pc.describe_index(index_name).status['ready']:
#     time.sleep(1)

# index = pc.Index(index_name)

# vectors = []
# for d, e in zip(data, embeddings):
#     vectors.append({
#         'id': d['id'],
#         'values': e['values'],
#         'metadata': {
#             'input': d['input'],
#             'output': d['output'],
#             'feedback': d['feedback']
#         }
#     })

# index.upsert(
#     vectors=vectors,
#     namespace="ns1"
# )
# print("data inserted")

# # Check data
# print(index.describe_index_stats())