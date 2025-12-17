# 🏦 **BankAccountSimulation — C# Multithreading Project**
*A real-world simulation of concurrent banking operations using threads, race condition handling, and synchronization.*

<p align="center">
  <img src="https://img.shields.io/badge/C%23-.NET%208.0-blue?logo=csharp&logoColor=white" />
  <img src="https://img.shields.io/badge/Threads-Multithreaded-purple" />
  <img src="https://img.shields.io/badge/Concepts-Synchronization%20%7C%20RaceConditions-yellow" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

<p align="center">
  <b>Thread safety</b> • <b>Shared resource synchronization</b> • <b>Race condition prevention</b> • <b>Realistic concurrent simulation</b>
</p>

---

# 🌟 **Overview**

**BankAccountSimulation** is a hands-on Operating Systems project built using **C# and .NET**, designed to demonstrate how multiple threads interact with a **shared resource** — a bank account.

The project simulates:

- 🔹 How **race conditions** occur  
- 🔹 How to prevent them using **critical sections**  
- 🔹 How **thread scheduling** leads to unpredictable behavior  
- 🔹 How to synchronize access using `lock`  
- 🔹 Realistic concurrent deposits & withdrawals  

This makes the project an excellent visualization of *core OS concepts* such as concurrency, synchronization, and shared memory issues.

---

# ✨ **Features**

### 🧵 **1. Multithreaded Client Simulation**
Each client runs in its own thread and performs randomized operations:

- Depositing money  
- Withdrawing money  
- Repeating operations with random delays  

This creates true concurrent behavior.

---

### 🔒 **2. Full Synchronization**
The shared `BankAccount` uses:

```csharp
lock (locker) { ... }
```

to ensure:

- Only **one thread** accesses the balance at a time  
- No overlapping writes  
- No corrupted or inconsistent values  

---

### 💸 **3. Realistic Banking Logic**
Includes error handling for:

- Negative deposits  
- Invalid withdrawals  
- Insufficient funds  

---

### 📊 **4. Detailed Logging**
Each operation prints a clear log:

```
[Client 7] Deposited 135. Balance = 500194
[Client 3] Withdrew 130. New balance = 500064
```

This visualizes true thread interleaving.

---

# 🗂️ **Project Structure**

```
BankAccountSimulation/
│
├── Program.cs          # Creates threads and starts simulation
├── BankAccount.cs      # Shared resource with synchronized methods
└── Client.cs           # Worker threads executing random operations
```

---

# 🚀 **How It Works**

1️⃣ User enters initial balance  
2️⃣ User chooses number of clients (threads)  
3️⃣ Each thread runs `DoWork()`  
4️⃣ Threads perform deposits and withdrawals  
5️⃣ Main thread waits for all threads using `Join()`  
6️⃣ Simulation ends cleanly  

---

# 🧪 **Sample Output**

```
[Client 10] Deposited 113. Balance = 499547
[Client 9] Withdrew 110. New balance = 499434
[Client 7] Deposited 135. Balance = 500194
All clients have completed their transactions.
```

Shows clean synchronization with natural concurrency.

---

# 🛠️ **Technologies Used**

- **C#**
- **.NET 8**
- **System.Threading**
- Critical sections (`lock`)
- Thread lifecycle & scheduling concepts

---

# 📌 **Learning Outcomes**

- Understanding multithreading  
- Identifying and preventing race conditions  
- Synchronization techniques  
- Safe shared-memory parallelism  
- OS-level concurrency fundamentals  

---

# 📈 **Future Enhancements**

✔ Add logging to file  
✔ Add multiple accounts per client  
✔ Replace `lock` with advanced primitives (Mutex, Monitor)  
✔ Visual UI for thread operations  
✔ Add custom scheduler simulation  

---

# 📄 **License**

Educational License.

---

# 👩‍💻 **Author**

**Kenzy Frhat**  
Faculty of Computers & Information — Year 2  

---

# ⭐ If this project helped you  
Give it a ⭐ on GitHub!
