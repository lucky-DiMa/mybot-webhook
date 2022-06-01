def check(simb):
    if len(simb) == 1:
        is_eng_or_n = False
        eng_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for l in range(0, len(eng_letters)):
            if simb == eng_letters[l].lower() or simb == eng_letters[l] or simb == '0' or simb == '1' or simb == '2' or simb == '3' or simb == '4' or simb == '5' or simb == '6' or simb == '7' or simb == '8' or simb == '9':
                is_eng_or_n = True
                break
        return is_eng_or_n
    else:
        return False