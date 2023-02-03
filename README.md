# HelloMachineLearning API

## 概要
HelloMachineLearningのAPIサーバー

## 使用技術
- Python
- Hug
- Amazon EC2

## 環境構築
1. Amazon EC2でインスタンスを用意
2. インスタンスのインバウンドルールを編集
3. `/api`フォルダをEC2インスタンスへアップロード
    ```
    $ scp -r -i kkk.pem api/ ec2-user@xx.xxx.xx.xxx:/home/ec2-user/api/
    ```
4. EC2インスタンスへ接続
    ```
    $ ssh -i kkk.pem ec2-user@xx.xxx.xx.xxx
    ```
5. EC2インスタンスにDockerを導入
    ```
    $ sudo yum install docker
    ```
6. Dockerイメージを作成
    ```
    $ cd api/
    $ sudo docker build --tag hello_machine_learning_api .
    ```
7. Dockerコンテナを起動
    ```
    $ pwd
    /home/ec2-user/api

    $ sudo docker run -it --rm -p 8000:8000 -v $(pwd)/app:/app hello_machine_learning_api
    ```


