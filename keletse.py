# Простий клас для управління банківськими рахунками
class BankAccount:
    def __init__(self, name, id_number, initial_balance):
        self.name = name
        self.id_number = id_number
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Поповнення: +{amount}")
        print(f"Успішно поповнено на {amount}. Новий баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Помилка: недостатньо коштів на рахунку!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Зняття: -{amount}")
            print(f"Успішно знято {amount}. Новий баланс: {self.balance}")

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Помилка: недостатньо коштів для переказу!")
        else:
            self.balance -= amount
            other_account.balance += amount
            self.transaction_history.append(f"Переказ до {other_account.id_number}: -{amount}")
            other_account.transaction_history.append(f"Переказ від {self.id_number}: +{amount}")
            print(f"Успішно переведено {amount} на рахунок {other_account.id_number}")

    def show_balance(self):
        print(f"Баланс рахунку {self.id_number}: {self.balance}")

    def show_transaction_history(self):
        print(f"Історія транзакцій для рахунку {self.id_number}:")
        for transaction in self.transaction_history:
            print(transaction)


# Простий банк для керування кількома рахунками
class SimpleBank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, id_number, initial_balance):
        if id_number in self.accounts:
            print(f"Помилка: Рахунок з ID {id_number} вже існує!")
        else:
            self.accounts[id_number] = BankAccount(name, id_number, initial_balance)
            print(f"Рахунок для {name} успішно створено з початковим балансом {initial_balance}.")

    def get_account(self, id_number):
        return self.accounts.get(id_number, None)


# Головна програма
def main():
    bank = SimpleBank()

    while True:
        print("\nМеню банку:")
        print("1. Створити рахунок")
        print("2. Поповнити рахунок")
        print("3. Зняти кошти")
        print("4. Переказати кошти")
        print("5. Переглянути баланс")
        print("6. Переглянути історію транзакцій")
        print("7. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ваше ім'я: ")
            id_number = input("Введіть ваш ID номер: ")
            initial_balance = float(input("Введіть початковий баланс: "))
            bank.create_account(name, id_number, initial_balance)

        elif choice == '2':
            id_number = input("Введіть ваш ID рахунку: ")
            account = bank.get_account(id_number)
            if account:
                amount = float(input("Введіть суму для поповнення: "))
                account.deposit(amount)
            else:
                print("Помилка: Рахунок не знайдено!")

        elif choice == '3':
            id_number = input("Введіть ваш ID рахунку: ")
            account = bank.get_account(id_number)
            if account:
                amount = float(input("Введіть суму для зняття: "))
                account.withdraw(amount)
            else:
                print("Помилка: Рахунок не знайдено!")

        elif choice == '4':
            sender_id = input("Введіть ваш ID рахунку: ")
            sender_account = bank.get_account(sender_id)
            if sender_account:
                receiver_id = input("Введіть ID рахунку отримувача: ")
                receiver_account = bank.get_account(receiver_id)
                if receiver_account:
                    amount = float(input("Введіть суму для переказу: "))
                    sender_account.transfer(receiver_account, amount)
                else:
                    print("Помилка: Рахунок отримувача не знайдено!")
            else:
                print("Помилка: Рахунок відправника не знайдено!")

        elif choice == '5':
            id_number = input("Введіть ваш ID рахунку: ")
            account = bank.get_account(id_number)
            if account:
                account.show_balance()
            else:
                print("Помилка: Рахунок не знайдено!")

        elif choice == '6':
            id_number = input("Введіть ваш ID рахунку: ")
            account = bank.get_account(id_number)
            if account:
                account.show_transaction_history()
            else:
                print("Помилка: Рахунок не знайдено!")

        elif choice == '7':
            print("Вихід...")
            break

        else:
            print("Невірний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()
