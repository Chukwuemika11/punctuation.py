from collections import Counter
import string

def clean_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower()

def word_count(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    # Count word occurrences
    word_counter = Counter(words)
    
    return word_counter

if __name__ == "__main__":
    filename = 'main.py'  # Replace with your file
    word_counts = word_count(filename)
    
    for word, count in word_counts.most_common(10):
        print(f'{word}: {count}')
