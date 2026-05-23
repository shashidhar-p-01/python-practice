def account_info(name, balance):
    return f"Account Holder: {name}, Balance: ${balance:.2f}"

def calculate_interest(balance, rate):
    return balance * (rate / 100)