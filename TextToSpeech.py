import os

if __name__ == '__main__':
    print("Welcome to text to speech converter")
    while True:
        str = input("Enter text to convert into speech: ")
        istr = str.upper()
        if istr == "QUIT":
            exit
        cmd = f"say {str}"
        os.system(cmd)
