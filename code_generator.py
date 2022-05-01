import random
def get_code(code_len=12):
    stop_index = ''
    code_str = ''
    for i in range(1, code_len):
        stop_index+='9'
    r = random.randint(1, int(stop_index))
    for i in range(0, 12 - len(str(r)), 1):
        code_str += '0'
    code_str += str(r)
    return code_str