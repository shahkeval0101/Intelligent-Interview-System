from collections import Counter
list1 = [
            "a Male, mood of speech: speaking passionately",
            "a female, mood of speech: Showing no emotion, normal",
            "a female, mood of speech: Showing no emotion, normal",
            "a Male, mood of speech: speaking passionately"
        ]
counter1 =  Counter(list1)
print(counter1)
print(counter1.most_common(1)[0][0])
