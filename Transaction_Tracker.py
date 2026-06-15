def after_transaction(balance, transaction):
    if balance + transaction < 0:
        return balance 
    else:
        return transaction + balance
       