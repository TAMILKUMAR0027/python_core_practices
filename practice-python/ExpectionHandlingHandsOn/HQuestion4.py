class PayOutOfBoundsException(Exception):
    pass

balance=80000
amount=20000

try:
    if amount>30000:
        raise PayOutOfBoundsException

    if amount>balance:
        raise PayOutOfBoundsException

    balance-=amount
    print("Withdrawal successful.")
    print("Updated balance:",balance)

except PayOutOfBoundsException:
    print("Error: Transaction amount exceeds insufficient balance.")