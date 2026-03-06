## 🐳 Docker Networking Lab

Hands-on demonstration of Docker container-to-container communication using a custom bridge network.

## 📌 Project Objective

The goal of this lab was to understand how Docker networking works internally by:

- Creating a custom bridge network

- Running multiple containers inside the same network

- Enabling DNS-based container name resolution

- Testing ICMP (ping) communication

- Testing HTTP service communication

- Handling container name conflicts

- Performing proper cleanup

## 🧱 Project Structure
```
docker-networking-lab/

│
├── README.md

└── screenshots/

    ├── 01-clean-environment.png

    ├── 02-network-created-devnet.png

    ├── 03-nginx-image-pulled.png

    ├── 04-container-name-conflict.png

    ├── 05-nginx-container-running.png

    ├── 06-alpine-container-started-successfully.png

    ├── 07-iputils-installed.png

    ├── 08-ping-web-success.png

    ├── 09-http-communication-success.png

    └── 10-lab-cleanup-complete.png
```
## 🔹 Step 1 — Verify Clean Environment

Checked existing containers before starting.
```
docker ps -a
```
📸

![Step 1](01-clean-environment.png)

## 🔹 Step 2 — Create Custom Bridge Network

Created a new Docker bridge network named devnet.
```
docker network create devnet
docker network ls
```
📸

![Step 2](02-network-created-devnet.png)

## 🔹 Step 3 — Deploy Nginx Container

Started an Nginx container attached to the custom network.
```
docker run -d --name web --network devnet nginx
```
Docker automatically pulled the image if not available locally.

📸

![Step 3](03-nginx-image-pulled.png)
## 🔹 Step 4 — Handle Container Name Conflict

Docker enforces unique container names.
Attempting to reuse a name results in a conflict error.

📸

![Step 4](04-container-name-conflict.png)
## 🔹 Step 5 — Verify Running Containers

Confirmed that the Nginx container is running.
```
docker ps
```
📸

![Step 5](05-nginx-container-running.png)
## 🔹 Step 6 — Launch Alpine Client Container

Started an interactive Alpine container inside the same network.
```
docker run -it --name client --network devnet alpine sh
```
📸

![Step 6](06-alpine-container-started-successfully.png)
## 🔹 Step 7 — Install Networking Utilities

Installed required networking tools inside Alpine.
```
apk add iputils wget
```
📸

![Step 7](07-iputils-installed.png)

## 🔹 Step 8 — Test Network Connectivity (ICMP)

Tested container-to-container communication using ping.
```
ping web
```
✔ Container name resolved via Docker DNS
✔ 0% packet loss
✔ Internal network communication successful

📸

![Step 8](08-ping-web-success.png)
## 🔹 Step 9 — Test HTTP Service Communication

Verified web service accessibility from Alpine.
```
wget -O- http://web
```
✔ Resolved to internal Docker IP (172.x.x.x)

✔ HTTP 200 OK response

✔ Nginx default page retrieved successfully

📸

![Step 9](09-http-communication-success.png)
## 🔹 Step 10 — Cleanup

Removed containers and network after lab completion.
```
docker rm -f web
docker network rm devnet
```

📸
![Step 10](10-lab-cleanup-complete.png)
## 🧠 Key Concepts Learned

- Custom bridge networks

- Docker embedded DNS server

- Container name resolution

- Inter-container communication

- ICMP vs HTTP connectivity testing

- Handling container name conflicts

- Professional lab cleanup workflow

## 🚀 Final Result

Successfully established container-to-container communication using a custom Docker bridge network.

This lab demonstrates practical Docker networking knowledge relevant to real-world DevOps and containerized environments.
