def count_vowels_consonants(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count
 

text = "Hello World 123!"
vowels, consonants = count_vowels_consonants(text)
print("Vowels:", vowels)
print("Consonants:", consonants)
