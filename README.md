# UDES Core Server

## Run with Docker

```bash
sudo docker build -t core-server .
sudo docker run -d -p 5000:5000 --network="host" --restart=always core-server
```