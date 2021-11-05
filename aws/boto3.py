import boto3

class S3:
    S3 = boto3.resource('s3')

    def __init__(self) -> None:
        pass

    def get_buckets(self):
        buckets = self.S3.buckets.all()
        for bucket in buckets:
            print(bucket.name)