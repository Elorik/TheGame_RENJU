def show_rules():
    print("=" * 50)
    print("         ГРА RENJU - ПЕРЕВІРКА ПЕРЕМОЖЦЯ")
    print("=" * 50)
    print()
    print("ПРАВИЛА ГРИ:")
    print("  - Поле 19x19 клітинок")
    print("  - Чорні камені позначаються цифрою 1")
    print("  - Білі камені позначаються цифрою 2")
    print("  - Порожня клітинка позначається цифрою 0")
    print("  - Перемагає той, хто поставить РІВНО 5")
    print("    каменів підряд (по горизонталі, вертикалі")
    print("    або діагоналі)")
    print("  - ВАЖЛИВО: 6 і більше підряд - НЕ перемога!")
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


def check_winner(board, color):
    """
    Перевіряє чи виграв гравець з вказаним кольором (1 або 2).
    Повертає (рядок, стовпець) першого каменя з п'ятірки, або None.
    """
    rows = 19
    cols = 19

    
    directions = [
        (0, 1),   # горизонталь
        (1, 0),   # вертикаль
        (1, 1),   # діагональ
        (-1, 1),  # діагональ
    ]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                # Кількість каменів
                count = 0
                for step in range(5):
                    r = row + dr * step
                    c = col + dc * step
                    if 0 <= r < rows and 0 <= c < cols and board[r][c] == color:
                        count += 1
                    else:
                        break

                # перевірка на 6
                if count == 5:
                    
                    before_r = row - dr
                    before_c = col - dc
                    before_ok = not (0 <= before_r < rows and 0 <= before_c < cols and board[before_r][before_c] == color)

                    
                    after_r = row + dr * 5
                    after_c = col + dc * 5
                    after_ok = not (0 <= after_r < rows and 0 <= after_c < cols and board[after_r][after_c] == color)

                    if before_ok and after_ok:
                        return (row + 1, col + 1)

    return None


def solve(board, case_number):
    """
    Визначає результат гри для одного поля і виводить результат.
    """
    print(f"--- Результат тесту #{case_number} ---")

    black_win = check_winner(board, 1)
    white_win = check_winner(board, 2)

    if black_win:
        print(1)
        print(black_win[0], black_win[1])
        print(f"Переможець: ЧОРНІ. Перший камінь п'ятірки: рядок {black_win[0]}, стовпець {black_win[1]}")
    elif white_win:
        print(2)
        print(white_win[0], white_win[1])
        print(f"Переможець: БІЛІ. Перший камінь п'ятірки: рядок {white_win[0]}, стовпець {white_win[1]}")
    else:
        print(0)
        print("Переможця ще немає.")
    print()


def main():
    show_rules()
    ask_ready()

    # Кількість тестових випадків
    while True:
        try:
            test_cases = int(input("Введіть кількість тестових випадків (від 1 до 11): "))
            if 1 <= test_cases <= 11:
                break
            else:
                print("Число повинно бути від 1 до 11!")
        except ValueError:
            print("Будь ласка, введіть ціле число!")

    print()

    for i in range(1, test_cases + 1):
        print(f"=== Тест #{i} ===")
        print("Введіть поле 19x19 (19 рядків, у кожному 19 чисел через пробіл):")
        print("  0 = порожньо, 1 = чорний камінь, 2 = білий камінь")
        print()

        board = []
        for row_num in range(1, 20):
            while True:
                try:
                    line = input(f"  Рядок {row_num}: ").split()
                    if len(line) != 19:
                        print(f"  Помилка: потрібно рівно 19 чисел, ви ввели {len(line)}. Спробуйте ще раз.")
                        continue
                    row = list(map(int, line))
                    if all(x in [0, 1, 2] for x in row):
                        board.append(row)
                        break
                    else:
                        print("  Помилка: числа повинні бути лише 0, 1 або 2. Спробуйте ще раз.")
                except ValueError:
                    print("  Помилка: введіть числа через пробіл. Спробуйте ще раз.")

        print()
        solve(board, i)

    print("=" * 50)
    print("Всі тести завершено. Дякуємо за гру!")
    print("=" * 50)


if __name__ == "__main__":
    main()