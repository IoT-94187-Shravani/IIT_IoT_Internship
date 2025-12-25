def main():
    text = input("Enter a string: ")

    # Basic indexing
    print("First character:", text[0])
    print("Last character:", text[-1])

    # Slicing examples
    print("\nSlicing Examples:")
    print("First 5 characters:", text[:5])
    print("Characters from index 2 to 6:", text[2:7])
    print("Characters from index 3 to end:", text[3:])
    print("Last 5 characters:", text[-5:])

    # Step slicing
    print("\nStep Slicing:")
    print("Every second character:", text[::2])
    print("Every third character:", text[::3])

    # Reverse string
    print("\nReversed string:", text[::-1])

    # User-defined slicing
    print("\nCustom Slice:")
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    step = int(input("Enter step value: "))

    print("Custom slice result:", text[start:end:step])


if __name__ == "__main__":
    main()