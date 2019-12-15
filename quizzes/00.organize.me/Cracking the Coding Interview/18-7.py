'''
18.7 - 주어진 단어 리스트에서, 다른 단어들을 조합하여 만들 수 있는 가장 긴 단어를 찾는 프로그램을 작성하라.
'''
sample_words = ['cat','banana','dog','nana','walk','walker','dogwalker']

def main():
    sample_words.sort(key=lambda x:len(x), reverse = True)
    for word in sample_words:
        filtered_words = sample_words[:]
        filtered_words.remove(word)
        if wordExist(word, filtered_words):
            return word
    else:
        return ''

def wordExist(word, sample_words):
    '''
    첫시작시: assert word1 not in sample_words
    '''
    if word in sample_words:
        return True
    for each in sample_words:
        if word.startswith(each):
            sub_word = word[len(each):]
            if wordExist(sub_word, sample_words):
                return True
    else:
        return False

print(main())
