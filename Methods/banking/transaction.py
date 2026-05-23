def transaction(amount, balance):
    if amount > balance:
        return "Insufficient funds"
    else:
        return f"Transaction successful. Remaining balance: ${balance - amount:.2f}"

def transfer(amount, from_balance, to_balance):
    if amount > from_balance:
        return "Insufficient funds for transfer"
    else:
        new_from_balance = from_balance - amount
        new_to_balance = to_balance + amount
        return f"Transfer successful. New balances - From: ${new_from_balance:.2f}, To: ${new_to_balance:.2f}"