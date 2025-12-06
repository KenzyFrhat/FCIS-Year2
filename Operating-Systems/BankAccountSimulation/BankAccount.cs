


namespace BankAccountSimulation
{
class BankAccount {
    private int balance = 0;
    private int id;
    private object locker = new object();

    public BankAccount(int initialBalance, int id)
    {
        balance = initialBalance;
        this.id = id;
    }
    
    public int Balance
{
    get
    {
        lock (locker)
        {
            return balance;
        }
    }
}

    public void Deposit (int amount){

        lock(locker){
            if(amount <= 0){
                throw new ArgumentException("Deposit amount must be positive");
            }

            balance += amount;
           
        }

    }

    public void Withdraw(int amount)
    {
        lock(locker){
            if(amount <= 0)
            {
                throw new ArgumentException("Withdrawal amount must be positive");
            }
            if(amount > balance)
            {
                throw new InvalidOperationException("Insufficient funds for this withdrawal");
            }
            balance -= amount;
           
        }
    }

}

}