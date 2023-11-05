# bedrock_extraction_data

Bedrockを使ってMySQLからデータを抽出する

## build and upcontainer
```bash
docker-compse up --build
```

## create DB user
ユーザーにはselect権限のみをつける
```sql
CREATE DATABASE bedrock;
CREATE USER if not exists 'bedrock_user'@'%' IDENTIFIED BY [password];
GRANT SELECT ON bedrock.* TO bedrock_user;
```


## create pre data

- コンテナに入る
```bash
docker exec -it dbedrock-demo /bin/bash
```

- データ作成
```bash
# テーブル作成
python pre_setting/models.py

# テストデータインサート
python pre_setting/insert_data.py
```
