from urllib.parse import urlparse, parse_qsl, parse_qs

o = urlparse('kafka://pkc-e8mp5.eu-west-1.aws.confluent.cloud:9092?topic=newtopic')
print(parse_qs(o.query))