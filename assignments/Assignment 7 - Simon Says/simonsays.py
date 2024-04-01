def simon_says(command):
    if command.startswith("Simon says"):
        print(command.split("Simon says", 1)[1].strip())

if __name__ == "__main__":
    while True:
        command = input().strip()
        simon_says(command)
