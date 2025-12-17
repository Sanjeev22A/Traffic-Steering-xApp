# OMNeT++ Installation Guide

A comprehensive guide to install OMNeT++ 6.3.0 on Linux systems.

## Step 1: Check Your Linux Version

Before starting the installation, verify your Linux distribution and version:

```bash
lsb_release -a
```
<img width="918" height="304" alt="image" src="https://github.com/user-attachments/assets/3e9032b2-8313-45e5-bcbd-2a33ae8db376" />

---

## Step 2: Download OMNeT++

Download the Linux-specific archive from the official website:

- Visit [https://omnetpp.org/download/](https://omnetpp.org/download/)
- Make sure you select the Linux-specific archive: `omnetpp-6.3.0-linux-x86_64.tgz`

![Step 2: Download OMNeT++](./images/image1.png)

---

## Step 3: Extract the Archive

Copy the archive to the directory where you want to install it (usually your home directory `/home/`). Open a terminal and extract the archive:

```bash
tar xvfz omnetpp-6.3.0-linux-x86_64.tgz
```



This will create an `omnetpp-6.3.0` subdirectory with the OMNeT++ files in it.

![Step 3: Extract the Archive](./images/image2.png)

---
<img width="928" height="549" alt="image" src="https://github.com/user-attachments/assets/9a2e8b25-c72a-4483-a954-3c39f5cbcf8f" />

## Step 4: Update System Packages

Update your system's package manager:

```bash
sudo apt update
```
<img width="904" height="1080" alt="Screenshot from 2025-10-28 16-25-16" src="https://github.com/user-attachments/assets/a675fbf0-5db2-42d2-a7b1-46065e01828d" />


![Step 4: Update System Packages](./images/image3.png)

---

## Step 5: Install Dependencies

Install all required build tools and libraries:

```bash
sudo apt-get install build-essential clang lld gdb bison flex perl python3 python3-pip qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libqt5opengl5-dev libxml2-dev zlib1g-dev doxygen graphviz libwebkit2gtk-4.0-37
```
<img width="921" height="453" alt="Screenshot from 2025-12-16 14-12-24" src="https://github.com/user-attachments/assets/e7370b37-ad6d-404f-b4ca-d11a09dc2fcc" />


![Step 5: Install Dependencies](./images/image4.png)

---

## Step 6: Install Python Packages

Install essential Python packages:

```bash
python3 -m pip install --user --upgrade numpy pandas matplotlib scipy seaborn posix_ipc
```
<img width="915" height="820" alt="Screenshot from 2025-12-16 14-14-33" src="https://github.com/user-attachments/assets/91c7d80a-7206-4563-8baf-6c32c91862cd" />

![Step 6: Install Python Packages](./images/image5.png)

---

## Step 7: Create a Virtual Environment

Open a terminal and create a Python virtual environment:

```bash
python3 -m venv .venv --upgrade-deps --clear --prompt "omnetpp/.venv"
```

---

## Step 8: Activate the Virtual Environment

Activate the virtual environment:

```bash
source .venv/bin/activate
```

---

## Step 9: Install Python Requirements

Install required Python packages using pip. It's also common to upgrade pip itself:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r python/requirements.txt
```

---
<img width="915" height="820" alt="Screenshot from 2025-12-16 14-28-35" src="https://github.com/user-attachments/assets/d74bde01-a619-4ea2-86e7-a040aa798ead" />

<img width="918" height="676" alt="Screenshot from 2025-12-16 14-36-38" src="https://github.com/user-attachments/assets/a256bde4-2a82-483c-9fe8-38cc395b6681" />

## Step 10: Set Up Environment Variables

OMNeT++ requires that certain environment variables are set and the `omnetpp-6.3.0/bin` directory is in the PATH. Source the setenv script to set up all these variables:

```bash
cd omnetpp-6.3.0
source setenv
```
<img width="879" height="111" alt="image" src="https://github.com/user-attachments/assets/3f8558e1-993d-4542-a8db-68f6889b279c" />

---

## Step 11: Configure the Build

The configure script detects installed software and the configuration of your system:

```bash
./configure
```

---

## Step 12: Compile OMNeT++

When `./configure` has finished, you can compile OMNeT++:

```bash
make
```

---

## Step 13: Verify Installation

Test the installation by running the Aloha example:

```bash
cd samples/aloha
./aloha
```

---
<img width="1845" height="1055" alt="Screenshot from 2025-12-17 14-48-36" src="https://github.com/user-attachments/assets/5cb5eaf7-0b43-4ed3-b77e-8c426f67a7e8" />

<img width="1845" height="1055" alt="image" src="https://github.com/user-attachments/assets/d5c6e1f6-267a-45e1-93ca-9f34c3384bf0" />

## Step 14: Start the IDE

To start the OMNeT++ IDE:

```bash
omnetpp
```
<img width="1845" height="1055" alt="image" src="https://github.com/user-attachments/assets/338fc85f-3a18-4277-931c-2b782a7674bb" />

---

## Step 15: Reconfigure and Rebuild Libraries

### Full Reconfiguration and Rebuild

If you need to reconfigure and rebuild everything:

```bash
./configure
make cleanall
make
```

### Rebuild a Specific Library

If you want to recompile just a single library, change to the directory of the library (e.g., `cd src/sim`) and type:

```bash
make clean
make
```

### Build Specific Modes

By default, libraries are compiled in both debug and release mode. If you want to make release or debug builds only, use:

**Release mode only:**
```bash
make MODE=release
```

**Debug mode only:**
```bash
make MODE=debug
```

---

For more information and advanced configuration options, visit the [official OMNeT++ website](https://omnetpp.org/).
