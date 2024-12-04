# よく使うコマンド

### Docker関連

#### Docker image の作成
```
docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -t QRcode-reader:latest .
```
※imageがビルドされたか確認
```
docker images
```

#### Docker container の立ち上げ
```
docker run -it --rm --gpus all --shm-size=64g --volume ~/research/QRcode-reader:/home/user qrcode:latest
```
※コンテナが立ち上がっているか確認
```
docker ps
```

#### Docker の基本操作
コンテナの確認
```
docker ps -a
```

コンテナの削除
```
docker rm [container ID]
```

イメージの削除
```
docker rmi [image ID]
```