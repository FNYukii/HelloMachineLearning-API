# HelloMachineLearning API

## 概要
HelloMachineLearningのAPIサーバー

## 使用技術
- Python
- Hug
- Amazon EC2

## 環境構築
### サーバーの用意(EC2を使う場合)
1. Amazon EC2でインスタンスを用意
2. インスタンスのインバウンドルールを編集
3. プロジェクトフォルダをEC2インスタンスへアップロード
    ```
    $ scp -r -i kkk.pem HelloMachineLearning-API/ ec2-user@xx.xxx.xx.xxx:/home/ec2-user/HelloMachineLearning-API/
    ```
4. EC2インスタンスへ接続
    ```
    $ ssh -i kkk.pem ec2-user@xx.xxx.xx.xxx
    ```
5. EC2インスタンスにDockerを導入
    ```
    $ sudo yum install docker
    ```

### hugサーバー起動
1. Dockerイメージを作成
    ```
    $ cd HelloMachineLearning-API/
    $ sudo docker build --tag hello_machine_learning_api .
    ```
2. Dockerコンテナを起動
    ```
    $ pwd
    /home/ec2-user/HelloMachineLearning-API

    $ sudo docker run -it --rm -p 8000:8000 -v $(pwd)/app:/app hello_machine_learning_api
    ```
