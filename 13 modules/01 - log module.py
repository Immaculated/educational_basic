from datetime import datetime

file_name = 'log_mike.txt'

def text(): # Text
    text = input('Enter the data:')
    return text

def log_mike( tag = ''):  # String in file
    with open(file_name,'a') as f:
        string = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") +' -'+' '+ text() + f'{tag}' + '. \n'
        f.write(string)

def log_mike_error():
    return log_mike(tag = 'Error') # String in file with Error tag

def log_mike_info():
    return log_mike(tag = 'Info') # String in file with Info tag