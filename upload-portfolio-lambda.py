import boto3
from botocore.client import Config
import StringIO
import zipfile

portfolio_bucket = s3.Bucket('stormageddon')
build_bucket = s3.Bucket('resumestormageddondarkness.com')

portfolio_zip = StringIO.stringIO()
build_bucket.download_fileobj('portfoliobuild.zip',portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
  for nm in myzip.namelist():
    obj = myzip.open(nm)
    portfolio_bucket.upload_fileobj(obj,nm)
    portfolio_bucket.Object(nm).Acl().pub(ACL='public-read')
