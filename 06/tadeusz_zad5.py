 # Wykorzystaj plik zawierający fragment Pana Tadeusza.
 # Znajdź najdłuższe słowo występujące w zadanym fragmencie.

filename = "tekst.txt"
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read().replace(",", "").replace("!", "").replace(".", "").split()

    print(content)
longest_word = ""
for word in content:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is: ", longest_word)
