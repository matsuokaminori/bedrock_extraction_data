import pprint
import boto3

# bedrock = boto3.client('bedrock')
bedrock = boto3.client("bedrock")
pprint.pprint(bedrock.list_foundation_models()["modelSummaries"])
