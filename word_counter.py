from collections import Counter


def read_large_file(file_path):
    word_counts = Counter()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                word_counts.update(word.lower() for word in line.split())
    return word_counts
