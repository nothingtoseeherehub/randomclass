import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes

import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes



def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:473673896446:randomclass')

    try:
    
        portfolio_bucket = s3.Bucket('stormageddon')
        build_bucket = s3.Bucket('resumestormageddondarkness.com')
        
        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj('portfolio.zip',portfolio_zip)
    
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj,nm)
    #    ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
    
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
                
        print "job done"
        topic.publish(Subject="test 2",Message="lambda message succeed")
    except:
        topic.publish(Subject="test 2",Message="lamba message fail")

    return 'Hello from Lambda'
