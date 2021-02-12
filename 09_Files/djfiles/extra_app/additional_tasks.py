STOP_WORDS = ['Это', 'слово', 'нельзя', 'Использовать']


def check_stop_words(file):
    file_lines = file.decode('utf-8').split('\n')
    for line in file_lines:
        line_lower = line.lower()
        for word in STOP_WORDS:
            if line_lower.find(word.lower()):
                return False
    return True
