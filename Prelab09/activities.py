from localBank import *

def loadBankData(dataFileName):
    bank = Bank()

    trans = list()
    with open(dataFileName, "r") as fp:
        for line in fp:
            data = getLine(line)
            if len(data) != 3:
                continue

            name = data[0]
            [fn, ln] = name.split()
            id = data[1]
            amt = data[2]

            bank.createAccount(fn, ln, id)

            if "(" in amt:
                amt = float(amt[2:-1])
                newTrans = Transaction("W", amt)
                trans.append((id, newTrans))
            else:
                amt = float(amt[1:])
                newTrans = Transaction("D", amt)
                trans.append((id, newTrans))

    for (id, tran) in trans:
        try:
            bank.applyTransaction(id, tran)
        except:
            pass

    return bank


def getLine(line):
    x = line.split("|")
    for i,y in enumerate(x):
        x[i] = y.strip()
    return x


def getTotalBalanceByPerson(bank, person):
    sum = 0
    for acc in bank.accounts.values():
        if acc.owner.firstName == person.firstName and acc.owner.lastName == person.lastName:
            sum = sum + acc.balance

    return sum

def getBalances(bank):
    pass


# temp = "Jimmy Smith          |     83545-99452     |    $104.98"
# print(getLine(temp))

# bank = loadBankData("transactions.txt")
# earl = Person("Earl", "Stewart")