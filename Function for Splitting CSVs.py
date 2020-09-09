import csv

def split_csv(source_path, dest_path, name, row_limit):
    '''
    creates csv files of length row_limit by splitting the original file into
    (file length / row limit) lines
    
    split_csv: Str Str Str Nat -> None
    '''
    source_file_path = source_path + '\\' + name +'.csv'
    source_file = open(source_file_path, 'r')
    reader = csv.reader(source_file)
    header = next(reader)
    file_number = 0
    lines= len(list(open(source_file_path)))
    max_file = lines / row_limit
    while file_number < max_file:
        i = 0
        file = dest_path + '\\' + name + '_' + str(file_number) +'.csv'
        with open(file, 'w', newline = '') as target:
            writer = csv.writer(target)
            while i < row_limit:
                if i == 0:
                    writer.writerow(header)
                try:
                    writer.writerow(next(reader))
                    i += 1
                except:
                    i+=1
        file_number += 1
    source_file.close()
