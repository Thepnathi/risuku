import boto3
import json

comprehend = boto3.client('comprehend')

text = "It is raining today in Seattle"

s = json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'))

print(comprehend)