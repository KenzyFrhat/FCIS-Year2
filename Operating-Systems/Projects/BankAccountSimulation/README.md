
🏦 BankAccountSimulation — C# Multithreading Project

A real-world simulation of concurrent banking operations using threads, race condition handling, and synchronization.

<p align="center"> <img src="https://img.shields.io/badge/Language-C%23-blue?logo=csharp&logoColor=white" /> <img src="https://img.shields.io/badge/.NET-8.0-purple?logo=dotnet&logoColor=white" /> <img src="https://img.shields.io/badge/Threads-Multithreaded-green" /> <img src="https://img.shields.io/badge/Status-Completed-success" /> </p> <p align="center"> <b>Thread safety</b> • <b>Shared resource synchronization</b> • <b>Race condition prevention</b> • <b>Realistic concurrent simulation</b> </p>
🌟 Overview

BankAccountSimulation is a practical Operating Systems project built with C#.
It simulates multiple clients (threads) performing deposits and withdrawals concurrently on a shared BankAccount resource.

The project demonstrates:

How race conditions occur

How to prevent them using lock (critical sections)

Thread scheduling behavior

Real-time balance updates

Randomized client operations for real-world realism

Perfect for understanding OS concepts like concurrency, synchronization, and shared memory problems.

✨ Features
🧵 1. Multithreaded Client Simulation

Each client runs in its own thread and performs randomized operations:

Deposits

Withdrawals

Mixed transactions

🔒 2. Full Synchronization

lock ensures:

Safe updates to shared balance

No overlapping writes

No inconsistent account states

💸 3. Realistic Banking Behavior

Insufficient funds detection

Positive amount validation

Random delays to mimic real user activity

📊 4. Detailed Logging

Every transaction prints:

[Client X] Deposited 120. Balance = 500340
[Client Y] Withdrew 87. New balance = 500253


This visualizes thread interleaving beautifully.

🗂️ Project Structure
BankAccountSimulation/
│
├── Program.cs          # Creates threads, starts simulation
├── BankAccount.cs      # Shared resource with synchronized methods
└── Client.cs           # Thread workers performing operations

🚀 How It Works
1️⃣ User chooses:

Initial balance

Number of clients (threads)

2️⃣ Program creates:

A shared BankAccount

N Client objects

N Threads executing DoWork()

3️⃣ Each client:

Randomly deposits or withdraws

Prints every operation

Sleeps briefly to simulate real delays

4️⃣ Main thread waits for all workers using Join()

Then prints final completion status.

🧪 Example Output
[Client 10] Deposited 113. Balance = 499547
[Client 6] Withdrew 76. New balance = 499356
[Client 3] Deposited 142. Balance = 500306
[Client 12] Withdrew 17. New balance = 498926
All clients have completed their transactions.


Shows true multithreading behavior — interleaving, unpredictability, and correctness ensured by synchronization.

🛠️ Technologies Used

C#

.NET 8

System.Threading

Thread lifecycle management

Synchronization primitives (lock)

Randomized workload simulation

📌 Learning Outcomes

This project helps students thoroughly understand:

Race conditions

Shared resource problems

Critical sections

Thread scheduling

Synchronization mechanisms

Why multithreading is hard without proper locking

🧭 Future Enhancements

Add UI dashboard to visualize thread operations

Support multiple accounts per client

Implement mutex or Monitor instead of lock

Add custom scheduler simulation

Log operations to file

📄 License

MIT License.

👩‍💻 Author

Kenzy Frhat
Operating Systems Project — Year 2
Faculty of Computers & Information