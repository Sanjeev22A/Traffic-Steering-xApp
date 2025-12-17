# OMNeT++ Installation Guide

A comprehensive guide to install OMNeT++ 6.3.0 on Linux systems.

## Prerequisites

### Check Your Linux Version

Before starting the installation, verify your Linux distribution and version:

```bash
lsb_release -a
```

## Installation Steps

### 1. Download OMNeT++

Download the Linux-specific archive from the official website:
- Visit [https://omnetpp.org/download/](https://omnetpp.org/download/)
- Download `omnetpp-6.3.0-linux-x86_64.tgz`

### 2. Extract the Archive

Copy the archive to your desired installation directory (typically `/home/`) and extract it:

```bash
tar xvfz omnetpp-6.3.0-linux-x86_64.tgz
```

This creates an `omnetpp-6.3.0` subdirectory containing all OMNeT++ files.

### 3. Update System Packages

Update your system's package manager:

```bash
sudo apt update
```

### 4. Install Dependencies

Install all required build tools and libraries:

```bash
sudo apt-get install build-essential clang lld gdb bison flex perl python3 python3-pip qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libqt5opengl5-dev libxml2-dev zlib1g-dev doxygen graphviz libwebkit2gtk-4.0-37
```

### 5. Install Python Packages

Install essential Python packages system-wide:

```bash
python3 -m pip install --user --upgrade numpy pandas matplotlib scipy seaborn posix_ipc
```

## Setting Up the Python Virtual Environment

### 6. Create a Virtual Environment

Create a Python virtual environment for OMNeT++:

```bash
python3 -m venv .venv --upgrade-deps --clear --prompt "omnetpp/.venv"
```

### 7. Activate the Virtual Environment

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### 8. Install Python Requirements

Upgrade pip and install required packages:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r python/requirements.txt
```

## Configuring OMNeT++

### 9. Set Up Environment Variables

Navigate to the OMNeT++ directory and source the setup script to configure environment variables and PATH:

```bash
cd omnetpp-6.3.0
source setenv
```

### 10. Configure the Build

Run the configuration script to detect your system's software and configuration:

```bash
./configure
```

### 11. Compile OMNeT++

Compile the framework:

```bash
make
```

## Verifying the Installation

### 12. Test the Installation

Navigate to the sample directory and run the Aloha example:

```bash
cd samples/aloha
./aloha
```

### 13. Start the IDE

Launch the OMNeT++ IDE:

```bash
omnetpp
```

## Reconfiguring and Rebuilding

### Clean Build

If you need to reconfigure and rebuild everything:

```bash
./configure
make cleanall
make
```

### Rebuild Specific Library

To recompile a specific library (e.g., the simulation library):

```bash
cd src/sim
make clean
make
```

### Build Specific Modes

By default, libraries are compiled in both debug and release modes. To build only a specific mode:

**Release mode only:**
```bash
make MODE=release
```

**Debug mode only:**
```bash
make MODE=debug
```

## Troubleshooting

If you encounter any issues during installation:
- Ensure all dependencies are properly installed
- Verify your Python version is 3.6 or higher
- Check that your virtual environment is activated before running pip commands
- Review the output of `./configure` for any missing dependencies

## Additional Resources

For more information and advanced configuration options, visit the [official OMNeT++ documentation](https://omnetpp.org/).
