import re
import sys
import textwrap
from io import StringIO
import boto3
from langchain.llms import Bedrock
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from database.extraction_data import execute_query


def print_ww(*args, width: int = 100, **kwargs):
    """Like print(), but wraps output to `width` characters (default 100)"""
    buffer = StringIO()
    try:
        _stdout = sys.stdout
        sys.stdout = buffer
        print(*args, **kwargs)
        output = buffer.getvalue()
    finally:
        sys.stdout = _stdout
    for line in output.splitlines():
        print("\n".join(textwrap.wrap(line, width=width)))


def get_ddl() -> str:
    with open("./table_ddl.sql", "r") as f:
        ddl = f.read()
    return ddl


def get_query(ddl: str, human_input: str) -> str:
    bedrock_client = boto3.client("bedrock-runtime")

    model_id = "anthropic.claude-instant-v1"
    llm = Bedrock(
        model_id=model_id,
        client=bedrock_client,
        model_kwargs={"max_tokens_to_sample": 1000},
    )

    template = """あなたはSQLマスターです。
質問に対して適切なSQLを返答してください。
使うデータベースのDDLは以下です。
SQLは改行せずに出力してください。
SQLは<sql>タグで囲んで出力してください。

<ddl>{ddl}</ddl>

Human: {human_input}
Assistant:"""

    prompt_template = PromptTemplate(
        input_variables=["ddl", "human_input"],
        template=template
    )
    prompt = prompt_template.format(
        ddl=ddl,
        human_input=human_input
    )
    # print(prompt)

    response = llm(prompt)
    return response


def extract_query(sql_string: str) -> str:
    """
    応答からクエリのみ抽出する
    """
    pattern = r'<sql>(.*?)</sql>'
    result = re.search(pattern, sql_string, re.DOTALL)

    if not result:
        return None

    query = result.group(1)
    return query


if __name__ == "__main__":

    ddl = get_ddl()
    human_input = "2023年９月中に購入された商品の合計金額を教えてください"
    sql_string = get_query(ddl, human_input)
    query = extract_query(sql_string)
    print_ww(query)

    execute_query(query)
