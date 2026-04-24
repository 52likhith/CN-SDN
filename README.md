# 📡 SDN Port Monitoring using POX & Mininet

NAME: M LIKHITH REDDY
SRN: PES1UG24CS282

This project demonstrates a **Software Defined Networking (SDN)** setup using **Mininet** and **POX controller**, where:

* Network topology is created using Mininet
* POX acts as the centralized controller
* A custom module (`port_monitor.py`) monitors switch port status
* The system detects **port UP/DOWN events**, logs them, generates alerts, and displays current status

---

##  Objectives

* Detect port up/down events
* Log changes with timestamps
* Generate alerts on failures
* Display real-time port status
* Demonstrate SDN control using POX

---

## 🧰 Requirements

### 🔹 Software

* Ubuntu/Linux (recommended)
* Python 3.x
* Mininet
* POX Controller

---

### 🔹 Install Mininet

```bash
sudo apt update
sudo apt install mininet
```

---

### 🔹 Clone POX

```bash
cd ~/Desktop
git clone https://github.com/noxrepo/pox.git
cd pox
```

---

## 📁 Project Structure

```
pox/
 ├── pox.py
 ├── forwarding/
 ├── misc/
 │    └── port_monitor.py   ← Your custom module
```

---

##  How to Run (Step-by-Step)

###  Step 1: Clean previous runs

```bash
sudo mn -c
sudo fuser -k 6633/tcp
sudo pkill -f pox
```

---

###  Step 2: Start POX Controller

```bash
cd ~/Desktop/pox
python3 pox.py forwarding.l2_learning misc.port_monitor
```

✔ Expected output:

```
POX 0.7.0 is up.
```

---

###  Step 3: Start Mininet (new terminal)

```bash
sudo mn --topo single,3 --controller=remote
```

---

###  Step 4: Test connectivity

```bash
mininet> pingall
```

✔ Expected:

```
0% dropped
```

---

###  Step 5: Generate traffic

```bash
mininet> h1 ping h2
mininet> h1 ping h3
```

---

###  Step 6: View flow rules

```bash
mininet> dpctl dump-flows
```

---

###  Step 7: Simulate link failure

```bash
mininet> link s1 h1 down
mininet> pingall
```

✔ Expected:

```
Packet loss (network disruption)
```

---

###  Step 8: Restore link

```bash
mininet> link s1 h1 up
```

---

## 📊 Features Demonstrated

### ✅ Port Event Detection

* Detects when a port goes UP or DOWN

### ✅ Logging

* Logs events with timestamps

### ✅ Alerts

```
ALERT: Port DOWN detected!
```

### ✅ Status Display

```
==== Current Port Status ====
Switch 1 Port 1 → DOWN
```

---

##  How It Works

* Mininet creates virtual hosts and switches
* Switch connects to POX controller
* `l2_learning` module enables packet forwarding
* `port_monitor.py` listens for port status changes
* Controller logs and reacts to network events

---

## ⚠️ Common Issues & Fixes

### ❌ Error: Address already in use (6633)

```bash
sudo fuser -k 6633/tcp
```

---

### ❌ pingall fails (100% dropped)

✔ Ensure you are running:

```bash
python3 pox.py forwarding.l2_learning misc.port_monitor
```

---

### ❌ Wrong commands in Mininet

* Only use Mininet commands inside `mininet>`
* Run Linux commands in normal terminal

---



## 🏁 Conclusion

This project demonstrates:

* Centralized control in SDN
* Real-time monitoring of network events
* Dynamic handling of link failures

---
