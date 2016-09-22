import csv, sys

if __name__ == '__main__':
    out_path, geo_path, other_paths = sys.argv[1], sys.argv[2], sys.argv[3:]
    
    print('Adjoining', out_path, 'from', geo_path, 'and',
           len(other_paths), 'other files', file=sys.stderr)
    
    geo_csv = csv.reader(open(geo_path, encoding='Latin-1'))
    other_csvs = [csv.reader(open(path, encoding='Latin-1')) for path in other_paths]
    
    with open(out_path, 'w', encoding='Latin-1') as out_file:
        out = csv.writer(out_file)
        
        for rows in zip(geo_csv, *other_csvs):
            geo_row, other_rows = rows[0], rows[1:]
            geoid = geo_row[48]
        
            out_row = geo_row[:]
        
            for other_row in other_rows:
                # Skip the identical first six fields of each other row.
                out_row.extend(other_row[6:])
            
            out.writerow(out_row)
