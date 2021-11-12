from aws.boto3 import S3
from bs4 import BeautifulSoup
import re

def filter_books(objs):
    str_book = 'lbr/book'
    if re.match(str_book, objs['key']):
        return True
    return False

# Book key
# book_key = 'lbr/book/053179a7fd544f1693cce8a2247bbdb3/OEBPS/modelos_comportamiento_epub-55.xhtml'
book_key = 'lbr/book/d1d36755bd2c457c9051ff038a59733b/c_01.html' # El abeto - Capitulo 1

s3 = S3()
s3.set_bucket('beereaders.com')
# s3.get_buckets()
# buck = s3.get_bucket()
# objs = buck.objects.all()
# for obj in objs:
#     print(obj)
obj = s3.get_object(book_key)
book_html = obj['Body'].read()
soup = BeautifulSoup(book_html, 'html')
print(soup.text)
