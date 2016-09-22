''' Index adjoined.csv into adjoined-index.csv.

Create a sorted file of GEOIDs with byte offsets and lengths of each record.
'''
import csv, io

geoids = {}

with open('adjoined.csv', mode='rb') as file:
    offset = 0
    for line in file:
        buff = io.StringIO(line.decode('Latin-1'))
        geoid = next(csv.reader(buff))[48]

        print('{0}: {1}-{2}'.format(geoid, offset, offset + len(line)))
        
        geoids[geoid] = offset, len(line)
        
        offset += len(line)

with open('adjoined-index.csv', mode='w') as file:
    out = csv.writer(file)
    for (geoid, (offset, length)) in sorted(geoids.items()):
        out.writerow((geoid, offset, length))

