import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1701804741236 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://aws-openaq-airquality-county/temp/openaqapi.json"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1701804741236",
)

# Script generated for node Amazon S3
AmazonS3_node1701804902577 = glueContext.write_dynamic_frame.from_options(
    frame=AmazonS3_node1701804741236,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://aws-glue-openaq-county-transformed",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1701804902577",
)

job.commit()
