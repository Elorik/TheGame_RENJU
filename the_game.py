BOARD_SIZE = 19
WIN_LENGTH = 5
MAX_TEST_CASES = 11

DIRECTIONS = [
    (0, 1, "горизонтально →"),
    (1, 0, "вертикально ↓"),
    (1, 1, "діагональ ↘ (зліва-верх → справа-низ)"),
    (-1, 1, "діагональ ↗ (зліва-низ → справа-верх)")
]


def show_rules():
    print("=" * 50)
    print("         ГРА RENJU - ПЕРЕВІРКА ПЕРЕМОЖЦЯ")
    print("=" * 50)
    print()
    print("ПРАВИЛА ГРИ:")
    print(f"  - Поле {BOARD_SIZE}x{BOARD_SIZE} клітинок")
    print("  - Чорні камені позначаються цифрою 1")
    print("  - Білі камені позначаються цифрою 2")
    print("  - Порожня клітинка позначається цифрою 0")
    print(f"  - Перемагає той, хто поставить РІВНО {WIN_LENGTH}")
    print("    каменів підряд (по горизонталі, вертикалі")
    print("    або діагоналі)")
    print(f"  - ВАЖЛИВО: {WIN_LENGTH + 1} і більше підряд - НЕ перемога!")
    print()
    print("ЩО ВИВОДИТЬ ПРОГРАМА:")
    print("  1 - перемогли чорні")
    print("  2 - перемогли білі")
    print("  0 - переможця ще немає")
    print("  + координати першого каменя з п'ятірки")
    print()
    print("=" * 50)


def ask_ready():
    while True:
        answer = input("Ви зрозуміли правила? (так/ні): ").strip().lower()
        if answer in ["так", "т", "yes", "y"]:
            print()
            print("Чудово! Починаємо гру.")
            print()
            break
        elif answer in ["ні", "н", "no", "n"]:
            print()
            show_rules()
        else:
            print("Введіть 'так' або 'ні'")


def is_valid_cell(board, r, c, color):
    """
    Перевіряє, чи клітинка (r, c) знаходиться в межах поля
    і містить камінь заданого кольору.
    """
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == color


def check_winner(board):
    """
    Перевіряє чи виграв гравець (1 або 2).
    Повертає (color, рядок, стовпець) першого каменя з п'ятірки, або None.
    """
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = board[row][col]
            if color == 0:
                continue
            for dr, dc, name in DIRECTIONS:
                # перевіряємо, чи це початок послідовності
                prev_r = row - dr
                prev_c = col - dc
                if is_valid_cell(board, prev_r, prev_c, color):
                    continue

                count = 0
                for step in range(WIN_LENGTH):
                    r = row + dr * step
                    c = col + dc * step
                    if is_valid_cell(board, r, c, color):
                        count += 1
                    else:
                        break

                if count == WIN_LENGTH:
                    after_r = row + dr * WIN_LENGTH
                    after_c = col + dc * WIN_LENGTH
                    if not is_valid_cell(board, after_r, after_c, color):
                        return color, row + 1, col + 1
    return None


def solve(board, case_number):
    """
    Визначає результат гри для одного поля і виводить результат.
    """
    print(f"--- Результат тесту #{case_number} ---")

    result = check_winner(board)

    if result:
        color, r, c = result
        print(color)
        print(r, c)
        if color == 1:
            print(f"Переможець: ЧОРНІ. Перший камінь п'ятірки: рядок {r}, стовпець {c}")
        else:
            print(f"Переможець: БІЛІ. Перший камінь п'ятірки: рядок {r}, стовпець {c}")
    else:
        print(0)
        print("Переможця ще немає.")
    print()


def read_board():
    """
    Зчитує поле 19x19. Можна вводити рядок за рядком або весь блок одразу.
    """
    board = []
    print(f"Введіть поле {BOARD_SIZE}x{BOARD_SIZE} (рядки через Enter):")
    for _ in range(BOARD_SIZE):
        while True:
            try:
                line = input().split()
                if len(line) != BOARD_SIZE:
                    print(f"  Помилка: потрібно рівно {BOARD_SIZE} чисел, ви ввели {len(line)}. Спробуйте ще раз.")
                    continue
                row = list(map(int, line))
                if all(x in [0, 1, 2] for x in row):
                    board.append(row)
                    break
                else:
                    print("  Помилка: числа повинні бути лише 0, 1 або 2. Спробуйте ще раз.")
            except ValueError:
                print("  Помилка: введіть числа через пробіл. Спробуйте ще раз.")
    return board


def main():
    show_rules()
    ask_ready()

    while True:
        try:
            test_cases = int(input(f"Введіть кількість тестових випадків (від 1 до {MAX_TEST_CASES}): "))
            if 1 <= test_cases <= MAX_TEST_CASES:
                break
            else:
                print(f"Число повинно бути від 1 до {MAX_TEST_CASES}!")
        except ValueError:
            print("Будь ласка, введіть ціле число!")

    print()

    for i in range(1, test_cases + 1):
        print(f"=== Тест #{i} ===")
        board = read_board()
        print()
        solve(board, i)

    print("=" * 50)
    print("Всі тести завершено. Дякуємо за гру!")
    print("=" * 50)


if __name__ == "__main__":
    main()