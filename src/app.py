import csv
import os
import boto3
from botocore.exceptions import ClientError
from create_sql_by_llm import create_query
from database.extraction_data import execute_query


BUCKET_NAME = os.getenv("BUCKET_NAME")


def output_csv(items):
    # CSVファイルに書き込む
    csv_file = './output/output.csv'

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(items)

    return csv_file


def upload_to_s3(local_file_path):
    s3 = boto3.client('s3')

    # アップロードするローカルファイルのパスとファイル名
    file_name = os.path.basename(local_file_path)
    s3_file_name = f'{file_name}'

    # ファイルをS3にアップロード
    s3.upload_file(local_file_path, BUCKET_NAME, s3_file_name)

    return s3_file_name


def generate_presigned_url(object_name, expiration=3600):
    # S3クライアントを作成
    s3 = boto3.client('s3')

    # 署名付きURLの生成
    try:
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': object_name},
            ExpiresIn=expiration
        )
    except ClientError as e:
        print(e)
        return None

    return presigned_url


if __name__ == "__main__":
    question = "2023年9月中に商品を購入した全ユーザーの一覧を出してください"
    query = create_query(question)

    result = execute_query(query)
    print(result)
    local_file_path = output_csv(result)

    s3_file_name = upload_to_s3(local_file_path)
    presigned_url = generate_presigned_url(s3_file_name)
    print("ここからダウンロード: ", presigned_url)
