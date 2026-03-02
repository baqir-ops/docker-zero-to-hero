## 📦 Day 01 – Docker Fundamentals
🚀 Introduction

On Day 01, I learned the core fundamentals of Docker including:

- What Docker is

- Difference between Virtual Machines and Containers

- Docker Architecture

- Image vs Container

- Basic Docker commands

This day focused on understanding how Docker works internally and practicing essential commands.

## 🧠 Theory Covered
## 🔹 What is Docker?

Docker is a containerization platform that allows applications to run in isolated environments called containers.

Containers package:

- Application code

- Dependencies

- Runtime

- System tools

This ensures applications run the same across all environments.

## 🔹 VM vs Container

| Virtual Machine | Docker Container |
|-----------------|------------------|
| Full OS | Shares host kernel |
| Heavy (GBs) | Lightweight (MBs) |
| Slow boot time | Starts in seconds |
| Requires hypervisor | Uses Docker Engine |

## 🔹 Docker Architecture

Docker consists of:

- Docker Client – where commands are executed

- Docker Daemon (dockerd) – manages images & containers

- Docker Registry – stores images (Docker Hub by default)

## 🔹 Image vs Container

- Image → Read-only template (blueprint)

- Container → Running instance of an image

Multiple containers can be created from one image.

## 💻 Hands-On Commands Practiced
```
docker --version
docker run hello-world
docker images
docker ps
docker ps -a
docker run -it ubuntu bash
docker run -d -p 8080:80 nginx
docker stop <container_id>
docker start <container_id>
docker rm <container_id>
```
## 🔍 What Happens When Running a Container?

When running:
```
docker run nginx
```
Docker automatically:

1.Checks for image locally

2.Pulls from Docker Hub if not available

3.Creates container

4.Assigns default bridge network

5.Starts container

6.Executes default CMD

## 📌 Key Learnings

- Containers share the host kernel.

- Images are immutable templates.

- Containers are lightweight and fast.

- Port mapping (-p) is required to access services from host.

- Stopping and removing a container does NOT delete the image.


## 🎯 Outcome of Day 01

By the end of Day 01, I can:

✔ Run containers

✔ Manage container lifecycle

✔ Understand Docker architecture

✔ Differentiate image and container

✔ Explain Docker working process
