import os, time

from flask import Flask, request, Response

from remote import RemoteFileObject as RFO
from find import find_index_key

INDEX_URL = os.environ.get('INDEX_URL') or 'http://localhost/~migurski/Census-Reporter/adjoined-index.csv'
DATA_URL = os.environ.get('DATA_URL') or 'http://localhost/~migurski/Census-Reporter/adjoined.csv'

app = Flask(__name__)

@app.route('/')
def index():
    index_file = RFO(INDEX_URL, block_size=512*1024)
    data_file = RFO(DATA_URL, block_size=512*1024)
    
    
    
    search_keys = set(request.args.get('geo_ids', '').split(','))
    
    records, index_times, data_times = [], [], []
    
    for search_key in sorted(search_keys):
        index_start = time.time()
        location = find_index_key(search_key, index_file, 0, index_file.length)
        index_times.append(time.time() - index_start)
        
        data_start = time.time()
        if location:
            offset, length = int(location[1]), int(location[2])
            data_file.seek(offset)
            records.append(data_file.read(length))
        data_times.append(time.time() - data_start)
    
    headers = {
        'Content-Type': 'text/plain',
        'X-Index-Times': ' '.join(['{:.6f}'.format(t) for t in index_times]),
        'X-Data-Times': ' '.join(['{:.6f}'.format(t) for t in data_times]),
        }
    
    return Response(b''.join(records), headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
