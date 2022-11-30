from storages.backends.s3boto3 import S3Boto3Storage  # type: ignore


class MediaStorage(S3Boto3Storage):
    bucket_name = "{{project_name}}"
    location = "media"
