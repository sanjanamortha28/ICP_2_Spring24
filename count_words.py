import os

def count_words(line):
    words = line.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Get the current working directory
current_directory = os.getcwd()

# Set the input file path relative to the current directory
input_file_path = os.path.join(current_directory, 'input.txt')

with open(input_file_path, 'r') as file:
    content = file.read()
    Ae = [line.strip() for line in content.split('\n')]

# Concatenate stripped elements into a single string
concatenated_string = " ".join(element.strip() for element in Ae)

# Strip again and get word count
word_count = count_words(concatenated_string)

# Set the output file path relative to the current directory
output_file_path = os.path.join(current_directory, 'output.txt')

# Write the content and word count to an output file
with open(output_file_path, 'w') as output_file:
    output_file.write("Input Content:\n")
    output_file.write(content + '\n\nWord_Count:\n')
    for word, count in word_count.items():
        output_file.write(f'{word}: {count}\n')

# Print the content of the input file
print("Content in file:")
print(content)

# Print the word count
print("\nWord_Count:")
for word, count in word_count.items():
    print(f'{word}: {count}')

print(f"\nOutput written to {output_file_path}")
