class Costumer:

    def __init__(self, costumer_id: str, personal_nbr: str, name: str):
        self._costumer_id = costumer_id
        self._personal_nbr = personal_nbr
        self._name = name

    @property
    def costumer_id(self) -> str:
        return self._costumer_id
    
    @property
    def personal_nbr(self) -> str:
        return self._personal_nbr
    
    @property 
    def name(self) -> str:
        return self._name

    def __str__(self) ->str:
        return f'Name: {self._name}, Personnummer: {self._personal_nbr}, Kundnummer: {self._costumer_id}'
    



class Account:
    #egenskaper

    kundnummer = 9 

    def __init__(self, costumer_id: str, account_nbr:int):
        self._costumer_id = costumer_id
        self._account_nbr = account_nbr
        self._balance = 0
    
    @property 
    def costumer_id(self) -> str:
        return self._costumer_id
    
    @property
    def account_nbr(self) -> int:
        return self._account_nbr 
    
    @property
    def balance(self) -> float:
        return self._balance
    

    def deposit(self, amount: float) -> bool:
        if float(amount) > 0:
            self._balance += amount
            return True
        return False
        

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False 

    def __str__(self) -> str:
        return f'Kontonummer: {self._account_nbr}, Saldo: {self._balance} ({self._costumer_id})'

class Bank:
    costumer_count = 10
    account_count = 1000

    def __init__(self):
        self._costumers = {}    #Kunder (attribut)
        self._accounts = {}     #Bankkonton (attribut)
        
        #self._costumer_id = 'C' + str(Bank.costumer_count)
        #Bank.costumer_count += 1
        #self._account_nbr = Bank.account_count
        #Bank.account_count += 1

    def add_costumer(self, name: str, personal_nbr:str) -> str | None:
        #self._name = name
        #self._personal_nbr = personal_nbr 

        for costumer in self._costumers.values():   #kollar cosumers i costumers
            if costumer.personal_nbr == personal_nbr:
                return None
        
        self._costumer_id = f'C{Bank.costumer_count}'
        Bank.costumer_count += 1

        new_costumer = Costumer(self._costumer_id, personal_nbr, name)
        self._costumers[self._costumer_id] = new_costumer
        
        return self._costumer_id
    
    def get_costumer(self, costumer_id: str) -> Costumer | None:
        return self._costumers.get(costumer_id, None)
    
        #if costumer_id not in self._costumers:
            #return None
        #for costumer_id in self._costumers:
            #return f'{self._costumer_id}: {self._costumers[self._costumer_id]}'

    def find_costumer_by_part_of_name(self, name_part: str) -> list[Costumer]:
        matchande_kunder = []

        for costumer in self._costumers.values():
            if name_part.lower() in costumer.name.lower():
                matchande_kunder.append(costumer)
        return matchande_kunder


    def create_account(self, costumer_id: str) -> int:
        if costumer_id not in self._costumers:
            return -1
            
        self._account_nbr = Bank.account_count
        Bank.account_count += 1

        new_account = Account(self._costumer_id, self._account_nbr)
        self._accounts[self._account_nbr] = new_account
        
        #new_account = Account(self._costumer_id, self._account_nbr)
        #self._accounts[self._costumer_id] = new_account
        
        return self._account_nbr

    def get_account(self, account_nbr: int) -> Account | None:
        return self._accounts.get(self._account_nbr, None)

    def remove_account(self, account_nbr: int) -> bool:
        if account_nbr in self._accounts:
            self._accounts.pop(account_nbr)
            return True
        else:
            return False


if __name__ == '__main__':
    #kund = Costumer('C10', '990714', 'Hanna')
    #print(kund)

    #kund = Account('C10','1000')
    #print(kund)

    kund = Bank()
    k2 = kund.add_costumer('Hanna', '990714')
    print(k2)
    k3 = kund.add_costumer('Anna', '980714')
    print(k3)
    h1 = kund.get_costumer('C10')
    print(h1)
    
    h2 = kund.create_account('C11')
    print(h2)
    h3 = kund.create_account('C10')
    print(h3)

    j1 = kund.get_account('1000')
    print(j1)

    print('hello\n')
    i1 = kund.find_costumer_by_part_of_name('ann')
    for costumer in i1:
        print(costumer)

    ta_bort = kund.remove_account(1000)
    print(ta_bort)

    i1 = kund.find_costumer_by_part_of_name('ann')
    for costumer in i1:
        print(costumer)
