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



