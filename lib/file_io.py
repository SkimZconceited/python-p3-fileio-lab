def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as log_file:
        log_file.write(file_content)
    pass

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as log_file:
        log_file.write(append_content)
    pass

def read_file(file_name):
    file_content = open(f'{file_name}.txt', encoding='utf-8')
    return file_content.read()
    pass

# write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
# append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")
# read_file(file_name="logfile")