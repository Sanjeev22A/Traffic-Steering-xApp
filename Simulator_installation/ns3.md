# Installing ns-3 and 5G Module on Ubuntu 22.04

This document describes the steps required to install **ns-3** on **Ubuntu 22.04**, along with the associated **5G module**.

---

## Step 1: Clone the ns-3 Repository

### Step 1.1:Clone the official **ns-3 development repository** from GitLab:

```bash
git clone https://gitlab.com/nsnam/ns-3-dev.git
cd ns-3-dev
```
By default, Git checks out the master branch, which is the active development branch. Since this branch may contain experimental features or unresolved bugs, it is recommended to switch to a stable release.

### Step 2: Checkout a Stable Release (ns-3.45)

In this guide, we use ns-3 release 3.45, which is a stable version.

Create and switch to a local branch based on the ns-3.45 release tag:
```bash
git checkout -b ns-3.45-release ns-3.45
```
### Step 3: Verify the Current Branch

To verify that you are working on the correct branch, run:
```bash
git branch
```
You should see output similar to the following, indicating that ns-3.45-release is the active branch:
<img width="484" height="77" alt="Git branch output" src="https://github.com/user-attachments/assets/0d516a68-bcd8-42fc-b943-f7cb05a192c8" />

## Step 2: Building and Testing ns-3
<br>

### Step 2.1: Configuring ns3
```bash
./ns3 configure --enable-examples --enable-tests
```
The output expected is shown below:
<img width="625" height="488" alt="image" src="https://github.com/user-attachments/assets/5c93b3d6-ef27-4624-8475-e3c0e756f6be" />
<img width="602" height="608" alt="image" src="https://github.com/user-attachments/assets/565b1690-4a7d-4cbe-a18a-83d76d272500" />
<br>
<br>
The set of modules that can be built and not built are shown in the figure. The not built modules are optional
<img width="799" height="271" alt="image" src="https://github.com/user-attachments/assets/18d60752-8682-4893-93e8-560be8fccbd0" />
<br>
<br>

### Step 2.2: Building the ns3

```bash
./ns3 build
```
<img width="593" height="74" alt="image" src="https://github.com/user-attachments/assets/eb91d791-dac7-4d8d-8002-e80a4bab4bd3" />

### Step 2.3: Run the testcases to ensure that the build has been successfull. Success means all the testcases pass
```bash
./test.py
```
<img width="348" height="617" alt="image" src="https://github.com/user-attachments/assets/ea750ff5-239f-4abe-ab1c-757d0182493a" />
<img width="622" height="669" alt="image" src="https://github.com/user-attachments/assets/307dfe77-9e03-4da9-b16a-f8f8ee030fef" />

## Step 3: Installing additional packages

### Step 3.1: Installing qt5
```bash
sudo apt update
sudo apt install snapd
sudo snap install qt5-core22
```

<img width="650" height="79" alt="image" src="https://github.com/user-attachments/assets/43c1ac02-3456-4baf-875c-8ed6f4a871bd" />
<br>

### Step 3.2: Installing sqlite3
```bash
sido apt update
sudo apt install sqllite3
```
<img width="738" height="363" alt="image" src="https://github.com/user-attachments/assets/464539bd-b76d-4fc5-87a5-3f8872fca0a1" />
### Step 3.3: Installing python venv and cppyy and python bindings
installing the necessary dependencies
```bash
sudo apt update
sudo apt install -y \
  build-essential \
  cmake \
  python3-dev \
  python3-venv \
  libclang-dev \
  llvm-dev \
  clang
```
<img width="918" height="817" alt="image" src="https://github.com/user-attachments/assets/08cba30d-9fe0-48aa-83e1-c0565f9ba836" />

Creating a virtual environment for python bindings for ns3
```bash
python3 -m venv ns3-pyenv
```
then check if venv is created or not
```bash
ls -a
```
<img width="918" height="202" alt="image" src="https://github.com/user-attachments/assets/d4182053-b166-47b0-9493-67f4237710fd" />

Then we start the virtual environment using the command
```bash
source ns3-env/bin/activate
```

<br>
check the version of venv using the command:
```bash
python --version
```
<img width="848" height="261" alt="image" src="https://github.com/user-attachments/assets/8a8aa381-580c-496b-9886-7fc8ccea349e" />


Install cppyy for python bindings in ns3

```bash
 pip install --upgrade pip setuptools wheel
pip install cppyy==3.1.2

```
Checking if cppyy instalation is correct
```bash
python - << EOF
import cppyy
print("cppyy version:", cppyy.__version__)
EOF
```
<img width="943" height="744" alt="image" src="https://github.com/user-attachments/assets/e822f809-9101-476d-9dcc-e852f83756f0" />

Configuring the python bindings
```bash
./ns3 configure --enable-python-bindings
```
<img width="930" height="840" alt="image" src="https://github.com/user-attachments/assets/8f967129-98a8-4b00-a56c-0b8ed2e993bf" />

Build ns3 again
```bash
./ns3 build
```
<img width="703" height="89" alt="image" src="https://github.com/user-attachments/assets/0c20d98f-5fd4-45d3-9756-edf246020cf7" />

Test the python bindings with a sample program
```bash
./ns3 run "examples/tutorial/first.py"
```
<img width="918" height="304" alt="image" src="https://github.com/user-attachments/assets/3b668c6d-52fd-47ac-9a14-8f4e0f668188" />
