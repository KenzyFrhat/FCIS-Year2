

namespace BankAccountSimulation
{

class Client
{   
    private int id;
    private BankAccount account;

    Random rand = new Random();

    public Client(int id, BankAccount account)
    {
        this.id = id;
        this.account = account;
    }

    public void Deposit(int amount)   
    {

        account.Deposit(amount);
        
    }

    public void Withdraw(int amount)
    {
     
        account.Withdraw(amount);
     
    }

    public void DoWork()
    {

        for(int i = 0; i < 10; i++)
        {
            int amount = rand.Next(1, 200);
            int choice = rand.Next(2);

            if(choice == 0)
            {
                Deposit(amount);
                 Console.WriteLine($"[Client {id}] Deposited {amount}. Balance = {account.Balance}");

            }
            else
            {
                Withdraw(amount);
                 Console.WriteLine($"[Client {id}] Withdrew {amount}. New balance = {account.Balance} ");
            }
            Thread.Sleep(rand.Next(100));  // Simulate some delay for simulate real world operations
        }

    }
}
}