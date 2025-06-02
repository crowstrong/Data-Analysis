while True:
    user_input = input("\n10. Введіть число для перевірки на простоту ('stop' для завершення): ")
    if user_input.lower() == 'stop':
        print("Завершення програми.")
        break

    if not user_input.isdigit():
        print("Будь ласка, введіть ціле додатнє число.")
        continue

    prime_check = int(user_input)
    is_prime = True

    if prime_check < 2:
        is_prime = False
    else:
        for i in range(2, int(prime_check ** 0.5) + 1):
            if prime_check % i == 0:
                is_prime = False
                break

    print("Число просте." if is_prime else "Число не є простим.")
