# OMNeT++ Installation and Execution Using Docker and Xpra

This document describes the steps to install **x11docker** and run **OMNeT++** as a Docker container using **Xpra** for GUI forwarding.

---

## 1. Install x11docker on Ubuntu (Recommended Method)

`x11docker` is not available via `apt`. It must be installed manually from the official repository.

### Step 1: Download the x11docker script

```bash
curl -fsSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker \
| sudo tee /usr/local/bin/x11docker > /dev/null
```

### Step 2: Make it executable

```bash
sudo chmod +x /usr/local/bin/x11docker
```

### Step 3: Verify installation

```bash
x11docker --version
```

---

## 2. OMNeT++ Docker Server (Xpra-enabled Image)

Run the OMNeT++ Docker container that exposes the Xpra server on port `9876`.

```bash
docker run -p 9876:9876 firejox/omnetpp-dock:xpra
```

**Explanation:**

* `9876` is the TCP port used by the Xpra server inside the container
* The port is forwarded to the host for client attachment

---

## 3. OMNeT++ Client (Xpra Attach)

Attach to the running OMNeT++ container from the host using Xpra.

```bash
xpra attach tcp://127.0.0.1:9876
```

or equivalently:

```bash
xpra attach tcp://localhost:9876
```

⚠️ **Note:**
Do **not** use `host` as the hostname. It is not a valid DNS name and will cause name resolution errors.

---

## Notes and Recommendations

* This setup works on **Wayland** and **Xorg**, but Xpra over TCP may have:

  * Keyboard mapping limitations
  * Clipboard restrictions
* For maximum stability (Qt, NetAnim, OMNeT++ IDE), consider:

  ```bash
  x11docker --xc -I firejox/omnetpp-dock
  ```

---

