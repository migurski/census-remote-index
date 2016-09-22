''' Index g20151-slice.csv into g20151-index.csv.

Create a sorted file of GEOIDs with byte offsets and lengths of each record.
'''
import csv, io

geoids = {}

with open('g20151-slice.csv', mode='rb') as file:
    offset = 0
    for line in file:
        buff = io.StringIO(line.decode('Latin-1'))
        _, _, _, _, _, geoid, _ = next(csv.reader(buff))

        print('{0}: {1}-{2}'.format(geoid, offset, offset + len(line)))
        
        geoids[geoid] = offset, len(line)
        
        offset += len(line)

with open('g20151-index.csv', mode='w') as file:
    out = csv.writer(file)
    for (geoid, (offset, length)) in sorted(geoids.items()):
        out.writerow((geoid, offset, length))

