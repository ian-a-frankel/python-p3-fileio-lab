def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode = 'w', encoding='utf-8') as overwriting_file:
        overwriting_file.write(file_content)

# with open('log_file.txt', mode='w', encoding='utf-8') as log_file:
#     log_file.write('Log 1')

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode = 'a', encoding='utf-8') as appending_file:
        appending_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", encoding='utf-8') as file_to_read:
        return(file_to_read.read())
