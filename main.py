def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    print(f"{count_words(file_contents)} words found in the document")
    print()

    lcs = count_letters(file_contents)
    for c in lcs:
        if c.isalpha():
            print(f"The '{c}' character was found {lcs[c]} times")

def count_words(str):
    return len(str.split())

def count_letters(str):
    letter_counts = {}
    for c in str:
        lc = c.lower()
        if lc not in letter_counts:
            letter_counts[lc] = 1
        else:
            letter_counts[lc] = letter_counts[lc] + 1
    return letter_counts

main()