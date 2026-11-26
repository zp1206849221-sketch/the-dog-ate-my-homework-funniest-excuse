import os

LINE = "You left it on the floor. In dog law, floor means mine. I didn't eat your homework — I legally repossessed my property."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
