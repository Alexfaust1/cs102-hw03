import sys
import csv

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    with open(input_file_path, mode= 'r') as file:
        csvread = csv.reader(file, delimiter = ',')
        for row in csvread:
            intlist = [float(i) for i in row]
            print(sum(intlist)/len(intlist))

if __name__ == "__main__":
    main()