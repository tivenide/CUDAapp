# CUDAapp
This repository contains the basic workflow for creating a containerized CUDA application with pytorch and docker.
The project was developed under Python 3.11 and Linux Ubuntu 22.04 lts.
## Installation / Prerequirements

Installation of docker. Check your version with:
```
docker -v
```
Installation of NVIDIA GPU drivers. Check your GPUs:
```
nvidia-smi
```

Set flag to using new buildsystem of docker (perhaps obsolete in the future).
```
echo \
'{
  "features": {
    "buildkit": true
  }
}' | sudo tee /etc/docker/daemon.json > /dev/null
```

[Installation of NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
)

Enable NVIDIA runtime
```
sudo nvidia-ctk runtime configure
sudo systemctl restart docker.service
```

## Usage
Building container
```
sudo docker build -t cudaapp:latest .
```
Running container
```
sudo docker run --gpus all cudaapp
```
