def anagram(w1,w2):
    if len(w1) != len(w2):
        return False
    else:
        list1 = list(w1)
        list2 = list(w2)

        list1.sort()
        list2.sort()

        idx = 0
        is_anagram = True

        while idx < len(w1) and is_anagram:
            if list1[idx]== list2[idx]:
                idx += 1
            else:
                is_anagram = False
        return is_anagram



def anagrams(word, words):
    for i in words:
        print word, i
        if anagram(word, i):
            print "are anagrams\n"




# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
