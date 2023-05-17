"""
File: scores.py
Name: Ryan Chung

-----------------------------
This program shows the corresponding scores for students
on final exam. A->90up; B->80~90; C->70~80; D-><70
"""


def main():
    score = int(input("Score: "))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("D")


# ---DO NOT EDIT THE CODE BELOW THIS LINE---

if __name__ == "__main__":
    main()
