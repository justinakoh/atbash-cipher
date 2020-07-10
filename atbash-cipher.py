from string import ascii_uppercase as l


def main():
    start_message = input(
        "This is an encoder/decoder which uses the AtBash Cipher. Do you wish to continue? "
    )
    if start_message == "" or start_message == "y" or start_message == "Y":
        # Create table with the alphabet reversed
        reversed_list = list(createTable())

        # Ask for input
        plaintext = input("Please enter your plaintext ")

        encoded_text = ""
        for i in plaintext:
            encoded_text += reversed_list[ord(i) - 97]

        # Output it
        print("The encoded text is: ", encoded_text)
        return encoded_text


# This reverses the alphabet refer to: https://stackoverflow.com/questions/509211/understanding-slice-notation for more information on slicing
def createTable():
    return str(l[::-1])

if __name__ == "__main__":
    main()
