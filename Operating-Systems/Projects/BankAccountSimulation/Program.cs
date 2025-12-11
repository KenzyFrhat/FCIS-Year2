namespace BankAccountSimulation{
class Program
{
    static void Main()
    {
        Console.WriteLine("--------Bank Account Simulation with Multiple Clients--------");

        Console.Write("Enter account ID: ");
        int accountId = int.Parse(Console.ReadLine());

        Console.Write("Enter initial balance: ");
        int initialBalance = int.Parse(Console.ReadLine());

        Console.Write("Enter number of clients (threads) : ");
        int numClients = int.Parse(Console.ReadLine());

        BankAccount account = new BankAccount(initialBalance, accountId);
        
        Client[] clients = new Client[numClients];
        Thread[] threads = new Thread[numClients];

        for(int i = 0; i < numClients; i++)
        {
            clients[i] = new Client(i + 1, account); // Pass the shared account to each client
            threads[i] = new Thread(clients[i].DoWork);

        }

        for(int i = 0; i < numClients; i++)
        {
            threads[i].Start();
        }

        for(int i = 0; i < numClients; i++)
        {
            threads[i].Join();
        }

        Console.WriteLine("All clients have completed their transactions.");

    }
}

}