import re
from langchain.chat_models import BedrockChat
from langchain.chains import create_sql_query_chain, LLMCheckerChain
from langchain.utilities import SQLDatabase
from langchain.llms import Bedrock
# from langchain.prompts import PromptTemplate
# from langchain_experimental.sql import SQLDatabaseChain
import boto3

user = "bedrock_abox"
password = "0323UserAbox-oi"
host = "db"
database = "bedrock"
charset = "utf8mb4"
DATABASE_URI = f"mysql://{user}:{password}@{host}:3306/{database}?charset={charset}"  # noqa: E501

db = SQLDatabase.from_uri(DATABASE_URI)
bedrock_client = boto3.client("bedrock-runtime")
model_id = "anthropic.claude-instant-v1"

bedrock_chat = BedrockChat(
    model_id=model_id,
    client=bedrock_client,
    model_kwargs={"max_tokens_to_sample": 1000},
)
bedrock_llm = Bedrock(
    model_id=model_id,
    client=bedrock_client,
    model_kwargs={"max_tokens_to_sample": 1000},
)


def create_sql_on_llm(bedrock_chat, question):

    chain = create_sql_query_chain(
        bedrock_chat,
        db,
        k=5,
    )

    response = chain.invoke(
        dict(
            question=question,
        )
    )
    return response


def extract_query(sql_string: str) -> str:
    """
    応答からクエリのみ抽出する
    """
    pattern = r'SQLQuery: (.+)'
    result = re.search(pattern, sql_string, re.DOTALL)

    if not result:
        return None

    query = result.group(1)
    return query


def create_query(question):
    """
    create query
    """

    # # question = "2023年9月中に購入した商品の総額はいくらですか？"
    response = create_sql_on_llm(bedrock_chat, question)
    query = extract_query(response)

    # query fact check
    checker_chain = LLMCheckerChain.from_llm(bedrock_llm, verbose=True)
    print(query, "\n", checker_chain.run(query))
    return query


if __name__ == "__main__":
    create_query("2023年8月中に商品を購入したすべてのユーザーの一覧を出してください")
