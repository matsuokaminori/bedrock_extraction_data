
# LLM

## LLMとは (2分)
LLM: 大規模言語モデル（Larg Language Model）
        = ラベル付けされていない大量のデータを用いて大規模なモデルを学習した「基盤モデル」のうち、言語に特化したもの

代表的なLLM) GPT-4(ChatGPTに搭載)、 PaLM(Bardに搭載)、Claude(10万トークンに対応)
※ 対応するトークン数が多いほど、長文を処理できる
トークン数を簡単に確認できる: https://platform.openai.com/tokenizer

従来の機械学習との違い: タスクごとにデータセットを用意してモデルを学習
                    　従来は特定の用途に特化したモデルだったため、ユースケースが限られていた

LLMの動作: 次の単語の予測を繰り返す。

## LLMを活用する
LLMが苦手なとこ: 
- 最新情報への対応
  - モデルが作成された時点までの情報した含まれない
- 出力の制御
  - 「この入力には必ずこの出力をしてほしい」への対応
- 妥当性の保証
  - 出力した内容が正しいかどうかはLLMにはわからない

LLMを活用するには：
- 入力(Prompt): プロンプトエンジニアリングによってLLMの性能を引き出す
感情を込めたプロンプトでパフォーマンスが上がる
https://aiboom.net/archives/58158

- LLM: LLMに含まれない情報はどうする？
- 出力(Completion): 独自のタスクに対応した出力にさせるには？


RAG: Retrieval Augmented Generation (RAG)
外部ソースから取得した情報を含めて LLM に出力を生成させる Prompt Engineering のテクニックの1つ

Fine-Tuning: 学習済みモデルを元に、特定のドメイン/タスクに 向けて追加データを用いて学習

https://pages.awscloud.com/rs/112-TZM-766/images/BG-3_llm_intro_tkyaaida_dist.pdf?version=0
https://pages.awscloud.com/rs/112-TZM-766/images/AD-3_AI_Day_for_Dev_Day3-03-LLM-usecase.pdf?version=0


# LangChain (1分)
言語モデルを利用したアプリケーション開発のためのフレームワーク

Python/TypeScriptに対応


- Model I/O: 言語モデルとのインターフェース
- Retrieval: アプリケーション固有のデータとのインターフェース
- Chains: 一連の呼び出しを構築する
- Agents: 与えられた高レベルのディレクティブを使用してチェーンにどのツールを使用するかを選択させます
- Memory: チェーンの実行間でアプリケーションの状態を保持する
- Callbacks: チェーンの中間ステップをログに記録してストリーミングする

https://python.langchain.com/docs/get_started/introduction



Bedrock


# デモ (2分)
「2023年9月中に商品を購入した全ユーザーの一覧がほしいんだけど」に瞬時に答えるアプリ
要件
- 自然言語(日本語)で入力
- 結果をCSVファイルに出力する

技術
- LangChain
- AWS Bedrock
基盤モデルを活用した 生成系AIアプリケーションを 簡単に構築、スケール
APIでBedrockで準備されている基盤モデルを利用可能



つくったもの:
- LLMでSQLを生成
- SQLAlchemyでSQLを実行
- CSVファイルに出力、s3にアップロード、署名付き一時URLを生成

LangChainのChainの一種、`create_sql_query_chain`でSQLを生成
LLMはAWS Bedrockの`Claude Instant`


注意事項
- 生成結果が正しい保証はない
- SQLが生成できない場合がある


https://github.com/matsuokaminori/bedrock_extraction_data.git
