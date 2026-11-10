import secrets
import string


def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    groups = []

    if use_lower:
        groups.append(string.ascii_lowercase)
    if use_upper:
        groups.append(string.ascii_uppercase)
    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append("!@#$%^&*()-_=+[]{};:,.?")

    if not groups:
        raise ValueError("حداقل یک نوع کاراکتر را انتخاب کن.")

    if length < len(groups):
        raise ValueError(
            f"طول رمز باید حداقل {len(groups)} باشد تا از هر نوع انتخاب‌شده یک کاراکتر داشته باشد."
        )

    # تضمین می‌کند از هر گروه انتخاب‌شده دست‌کم یک کاراکتر در رمز باشد.
    password_chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)

    password_chars.extend(
        secrets.choice(all_chars) for _ in range(length - len(password_chars))
    )

    # ترتیب کاراکترها را به‌صورت امن به‌هم می‌زند.
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


try:
    length = int(input("طول رمز چند کاراکتر باشد؟ "))

    if length <= 0:
        print("طول رمز باید بیشتر از صفر باشد.")
    else:
        lower = input("حروف کوچک داشته باشد؟ (بله/خیر): ").strip().lower() == "بله"
        upper = input("حروف بزرگ داشته باشد؟ (بله/خیر): ").strip().lower() == "بله"
        digits = input("عدد داشته باشد؟ (بله/خیر): ").strip().lower() == "بله"
        symbols = input("نماد داشته باشد؟ (بله/خیر): ").strip().lower() == "بله"

        password = generate_password(length, lower, upper, digits, symbols)
        print("\nرمز ساخته‌شده:", password)

except ValueError as error:
    print("خطا:", error)