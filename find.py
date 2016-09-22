''' Search for records in g20151-slice.csv using index g20151-index.csv.

Also search for a few junk records, to make sure they're not found.
'''
import csv, os, io

def read_csv_line(file):
    ''' Reurn one line of comma-separated data from the current file position.
    '''
    line = b''
    
    while True:
        line += file.read(1)
        if line[-1:] == b'\n':
            break
    
    rows = csv.reader(io.StringIO(line.decode('utf8')))
    return next(rows)

def seek_to_line_start(file, start):
    ''' Walk backwards in the file until the start of the current line.
    '''
    while file.tell() > start:
        char = file.read(1)
        if char == b'\n':
            break
        file.seek(-2, 1)

def find_index_key(search_key, file, f_start, f_end):
    ''' Find and return a row from an open file starting with the search key.
        
        File is assumed to be comma-separated and alphabetically ordered.
    '''
    # print('find_index_key(', f_start, f_end, ') for', f_end - f_start)
    
    if f_end == f_start:
        # Not going to find anything in a zero-length section of file.
        return None
    
    # Look for the row in the middle of the current file span.
    file.seek(f_start//2 + f_end//2, 0)
    seek_to_line_start(file, f_start)

    f_middle, row = file.tell(), read_csv_line(file)
    
    # Did we find it?
    if search_key == row[0]:
        # print('Found', row)
        return row
    
    # Is the search key is before the current row?
    if search_key < row[0]:
        if f_middle == f_end:
            # We are about to repeat ourselves, so we've found nothing.
            return None

        # Look into the first half of the current file span.
        return find_index_key(search_key, file, f_start, f_middle)
    
    # Is the search key is after the current row?
    if search_key > row[0]:
        if f_middle == f_start:
            # We may be stuck in a short segment of file, so jump forward one record.
            return find_index_key(search_key, file, file.tell(), f_end)

        # Look into the second half of the current file span.
        return find_index_key(search_key, file, f_middle, f_end)

for bogus_key in ('  ', '999', 'zzz', '000', 'aaa'):
    with open('g20151-index.csv', mode='rb') as file:
        length = os.stat(file.name).st_size
        found_row = find_index_key(bogus_key, file, 0, length)
        
        if found_row is not None:
            raise Exception('Incorrectly found {}'.format(repr(bogus_key)))

with open('g20151-index.csv') as test_file:
    rows = csv.reader(test_file)
    for (search_key, _, _) in rows:
        with open('g20151-index.csv', mode='rb') as index_file:
            length = os.stat(index_file.name).st_size
            found_row = find_index_key(search_key, index_file, 0, length)
            
            if found_row[0] != search_key:
                raise Exception('Failed to find {}'.format(search_row[0]))
            
            offset, length = int(found_row[1]), int(found_row[2])
            
            with open('g20151-slice.csv', mode='rb') as other_file:
                other_file.seek(offset)
                print(search_key, 'is in', (offset, length), 'of', repr(other_file.read(length)))
