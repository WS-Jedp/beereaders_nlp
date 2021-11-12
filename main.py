from aws.boto3 import S3
import re

def filter_books(objs):
    str_book = 'lbr/book'
    if re.match(str_book, objs['key']):
        return True
    return False

# Book key
book_key = 'lbr/book/053179a7fd544f1693cce8a2247bbdb3/OEBPS/modelos_comportamiento_epub-55.xhtml'

s3 = S3()
s3.set_bucket('beereaders.com')
# s3.get_buckets()
# buck = s3.get_bucket()
# objs = buck.objects.all()
# for obj in objs:
#     print(obj)
obj = s3.get_object(book_key)
print(obj['Body'].read())
