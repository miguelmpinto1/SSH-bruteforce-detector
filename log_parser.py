import re
from datetime import datetime

def parse_log_line(line):
    ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    date_match = re.search(r'[A-Za-z]{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}', line)

    if ip_match is None or date_match is None:
        return None

    ip = ip_match.group()
    date = date_match.group()    
    year = datetime.now().year
    full_timestamp = f"{year} {date}"
    timestamp = datetime.strptime(full_timestamp, "%Y %b %d %H:%M:%S")
    return ip, timestamp

def read_log_file(path):
    with open(path, 'r') as file:
        for line in file:
            clean_line = line.strip()
            result = parse_log_line(clean_line)
            if result == None:
                continue
            else:
                yield result
                
for evento in read_log_file("sample.log"):
    print(evento)
