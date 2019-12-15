'''
10.2- 철자 순서만 바꾼 문자열이 서로 인접하도록 문자열 배열을 정렬하는 메서드를 작성하라.
'''
sentence = 'What is life I dont know what to do I want to work for google and embrace the better and broader world in front of me'
words_in_order = sentence.split(' ')

words_sorted = sorted(words_in_order, key=lambda word:(len(word),sorted(list(word))))
print(words_sorted)
