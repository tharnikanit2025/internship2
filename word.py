import re
from collections import Counter
try:
    with open("sample.txt", "r") as file:
        text = file.read().lower()
    words = re.findall(r"\b\w+\b", text)
    frequency = Counter(words)
    print("\n===== WORD FREQUENCY =====")
    if not frequency:
        print("The file is empty!")
    else:
        for word, count in frequency.most_common():
            print(word, ":", count)
except FileNotFoundError:
    print("Error: sample.txt not found!")
except OSError:
    print("Error reading the file!")
