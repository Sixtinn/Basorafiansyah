def decimal_to_seven_segment(n):
    segments = [
        [1, 1, 1, 0, 1, 1, 1],  # 0
        [0, 0, 1, 0, 0, 1, 0],  # 1
        [1, 0, 1, 1, 1, 0, 1],  # 2
        [1, 0, 1, 1, 0, 1, 1],  # 3
        [0, 1, 1, 1, 0, 1, 0],  # 4
        [1, 1, 0, 1, 0, 1, 1],  # 5
        [1, 1, 0, 1, 1, 1, 1],  # 6
        [1, 0, 1, 0, 0, 1, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 1, 0, 1, 1],  # 9
    ]

    return segments[n] if 0 <= n < 10 else None

def print_seven_segment(segment):
    horizontal = "=====\n"
    vertical = "|| "

    for i in range(len(segment)):
        if i % 3 == 0 or i == 0:
            print(horizontal, end="")
        else:
            print(vertical if segment[i] == 1 else "   ", end="")
            if i == 2 or i == 5:
                print()

def draw_table(segment):
    print("===============================")
    print("|| a | b | c | d | e | f | g ||")
    print("-------------------------------")
    print("|| " + " | ".join(map(str, segment)) + " ||")
    print("===============================")

print("\n=========== Decimal to Seven_Segment ===========")
print("Name     : Baso Rafiansyah")
print("NIM      : D121231068")
print("Class    : B")
print("\n================ INFORMATIKA ===================")

while True:
    n = int(input("Enter number to display (0-9), input else to exit: "))
    
    if 0 <= n < 10:
        segment = decimal_to_seven_segment(n)
        print(f"{n} to Seven_Segment Representation in Table : ")
        draw_table(segment)
        print(f"Seven_Segment Display of {n} : ")
        print_seven_segment(segment)
        print()
    else:
        print("\nProgram End\n")
        break
