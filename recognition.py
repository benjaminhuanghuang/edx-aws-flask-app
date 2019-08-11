import pprint
import boto3

from PIL import Image, ImageDraw
rek = boto3.client('rekognition')

with open('Monalisa.jpg', 'rb') as f:
  image_bytes = f.read()

response = rek.detect_labels(
  Image = {
    'Bytes' : image_bytes
  }
)

pprint.pprint(response)

response = rek.detect_facess(
  Image = {
    'Bytes' : image_bytes
  },
  Attributes = ["ALL"]
)

