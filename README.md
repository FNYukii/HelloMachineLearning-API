# HelloMachineLearning API

## 概要
HelloMachineLearningのAPIサーバー

## 使用技術
- Python
- Hug
- Amazon EC2

## 環境構築
1. Dockerイメージを作成
    ```
    $ cd api/
    $ sudo docker build --tag hello_machine_learning_api .
    ```
2. Dockerコンテナを起動
    ```
    $ pwd
    /home/ec2-user/api

    $ sudo docker run -it --rm -p 8000:8000 -v $(pwd)/app:/app hello_machine_learning_api
    ```


