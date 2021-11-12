import boto3

class S3:
    S3 = boto3.client('s3')
    _current_bucket = ''
    bucket = None

    def __init__(self) -> None:
        pass

    def get_buckets(self):
        buckets = self.S3.buckets.all()
        for bucket in buckets:
            print(bucket.name)

    def set_bucket(self, name: str) -> None:
        self._current_bucket = name

    def get_bucket(self):
        self.bucket = self.S3.Bucket(self._current_bucket)
        return self.bucket

    def get_bucket_objects(self):
        return self.bucket.objects.all()

    def get_list_buckets(self):
        s3 = boto3.client('s3')
        resp = s3.list_buckets()
        for bucket in resp['Buckets']:
            print(f'Bucket -> {bucket}')

    def get_object(self, object: str):
        return self.S3.get_object(Bucket=self._current_bucket, Key=object)