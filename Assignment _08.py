
def count_lines(filename):
    count = 0

    with open(filename, "r") as file:
        for line in file:
            count += 1

    return count


def extract_first_two_lines(filename):
    first_two_lines = []

    with open(filename, "r") as file:
        for i, line in enumerate(file):
            if i < 2:
                first_two_lines.append(line)
            else:
                break

    return first_two_lines


def write_to_new_file(filename, data):
    with open(filename, "w") as file:
        for line in data:
            file.write(line)




input_file = input("Enter the input file name: ")


output_file = input("Enter the output file name: ")


try:

    # Step 1: Count the number of lines
    total_lines = count_lines(input_file)

    print("\n----------------------------------------------")
    print("Total number of lines:", total_lines)



   
    first_two_lines = extract_first_two_lines(input_file)

    print("\nFirst two lines of the file:")

    if len(first_two_lines) == 0:
        print("The file is empty.")

    else:
        for line in first_two_lines:
            print(line.strip())


    
    write_to_new_file(output_file, first_two_lines)

   
    print("First two lines have been successfully")
    print("written to:", output_file)
    


    
    print("\nContents of the new file:")

    with open(output_file, "r") as file:
        data = file.read()
        print(data)


except FileNotFoundError:
    print("\nError: Input file does not exist.")

except Exception as e:
    print("\nAn error occurred:", e)

