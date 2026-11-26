import os

LINE = "Your honour, the homework smelled of bacon grease and poor supervision. It was on the floor, and under dog law the floor is a buffet with no cover charge. I plead adorable."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
