x = 0
with open('alice.txt') as program:
    for line in program:
        words = line.split()
        x += len(words)
print("There are" , x , 'words in alice')


with open('alice.txt') as file:
    total_words = 0
    num_lines = 0
    for line in file:
        words = line.split()
        total_words += len(words)
        num_lines += 1

    avg_words = total_words / num_lines
    print("The average number of words per line is:", avg_words)

count = 0
maxcount = 15
with open('alice.txt') as book:
    for line in book:
        count = len(line.split())
        if count > maxcount:
                    maxline = line
                    maxcount = count
                    print('The longest line has',maxcount,'words:',maxline)



prompt = input('Enter word:')
with open('alice.txt', "r") as file:
    for line in file:
        if prompt in line:
            print(line)
