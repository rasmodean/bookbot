

def main():

    path_to_frankenstein = './books/frankenstein.txt'
    file_contents = get_text(path_to_frankenstein)
    word_count = count_words(file_contents)
    char_counts = get_char_counts(file_contents)
    char_list = get_list_dicts(char_counts)
    char_list.sort(reverse=True, key=sort_on)
    report = get_report(path_to_frankenstein, word_count, char_list)

    print(report)

    


def count_words(text):
    
    words = text.split(' ')
    return len(words)


def get_text(path):

    with open(path) as f:
        file_contents = f.read()
    return file_contents
    


# String -> Dict
def get_char_counts(text):
    
    text = text.lower()
    chars = {}

    for c in text:
        if c.isalpha() == False: continue 
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars


def get_list_dicts(my_dict):

    list_dicts = []

    for key in my_dict:

        char_dict = {'letter' : key, 'count' : my_dict[key]}
        list_dicts.append(char_dict)
    return list_dicts


def sort_on(dict):
    return dict["count"]


# String Dict -> String
def get_report(book_path, word_count, char_list):

    begin = f'--- Begin report of {book_path} ---\n'
    pword_count = f'{word_count} words found in the document\n\n'
    body = ''
    end = '--- End report ---'

    for cdict in char_list:
        letter = cdict['letter']
        count = cdict['count']
        body += f'The {letter} character was found {count} times\n'

    return begin + pword_count + body + end




main()

