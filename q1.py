initial_balance = int(input())
no_of_op = int(input())


# 
av_bal = initial_balance
uncommitted = []
commits = []

def read():
    print(av_bal)

def credit(amount):
    global av_bal
    av_bal += int(amount)
    uncommitted.append(("credit", int(amount)))

def debit(amount):
    global av_bal
    av_bal -= int(amount)
    uncommitted.append(("debit", int(amount)))

def abort(index):
    global av_bal
    if index <= len(uncommitted):
        operation, amount = uncommitted[index - 1]
        if operation == "credit":
            av_bal -= amount
        elif operation == "debit":
            av_bal += amount
        uncommitted.pop(index - 1)

def rollback(index):
    global av_bal
    if index <= len(commits):
        av_bal = commits[index - 1]

def commit():
    global uncommitted
    commits.append(av_bal)
    uncommitted.clear()

for i in range(no_of_op):
    o=input().split()
    operation = o[0]
    if operation == "read":
        read()
    elif operation == "credit":
        credit(o[1])
    elif operation == "debit":
        debit(o[1])
    elif operation == "abort":
        abort(int(o[1]))
    elif operation == "rollback":
        rollback(int(o[1]))
    elif operation == "commit":
        commit()
read()