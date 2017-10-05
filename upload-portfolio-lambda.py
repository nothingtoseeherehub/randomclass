import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes



def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:473673896446:randomclass')

    location = {
        "bucketName": "resumestormageddondarkness.com",
        "objectKey": "portfolio.zip"
    }
    try:
        job = event.get("CodePipeline.job")
        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3Location"]

        print "Building portfolio from " + str(location)
        portfolio_bucket = s3.Bucket('stormageddon')
        build_bucket = s3.Bucket(location["bucketName"])
# line 27 error questionmark

        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj(location["objectKey"],portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
    
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print "job done"
        topic.publish(Subject="Portfolio deployed",Message="lambda portfolio deployed succeed")
        if job:
            codepipeline = boto3.client("codepipeline")
            codepipeline.put_job_success_result(jobId=job["id"])

    except:
        topic.publish(Subject="Portfolio not deployed ",Message="lamba message fail")

    return 'Hello from Lambda'
