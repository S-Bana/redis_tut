from redis import Redis
import json
import time


redis_host = 'localhost'
redis_port = 6379
redis_pass = ""
redis_db = 0

rd = Redis(host=redis_host, port=redis_port, password=redis_pass, db=redis_db)

# remove all data from all databases
rd.flushall()

# rd.set('name', 'eli')
# rd.set('age', 18)

# x = rd.get('name')
# print(x)


# load jason 
with open('persons.json') as p:
    data = json.load(p)

# =====================================================================================
# normal 

# Record the start time
start_time = time.time()

for id, person in enumerate(data):
    rd.set(id, str(person))

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Execution Time: {elapsed_time:.4f} seconds")


# =====================================================================================
# piplining

# Record the start time
start_time = time.time()

# make a pipline
with rd.pipeline(data) as pipe:
    for id, person in enumerate(data):
        pipe.hsetnx('persons', id, str(person))
    pipe.execute()

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Execution Time: {elapsed_time:.4f} seconds")
