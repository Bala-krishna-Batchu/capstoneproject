import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1697998925238 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://aws-openaq-airquality-county/temp/tempairq.csv"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1697998925238",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1697998965670 = DynamicFrame.fromDF(
    AmazonS3_node1697998925238.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1697998965670",
)

# Script generated for node Change Schema
ChangeSchema_node1700789432112 = ApplyMapping.apply(
    frame=DropDuplicates_node1697998965670,
    mappings=[
        ("year", "string", "year", "int"),
        ("month", "string", "month", "int"),
        ("day", "string", "day", "int"),
    ],
    transformation_ctx="ChangeSchema_node1700789432112",
)

# Script generated for node Amazon S3
AmazonS3_node1697998973307 = glueContext.getSink(
    path="s3://aws-glue-openaq-county-transformed/openaqtransformed/finaltransformed/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    compression="gzip",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1697998973307",
)
AmazonS3_node1697998973307.setCatalogInfo(
    catalogDatabase="airqdatabase", catalogTableName="aws-glue-openaqtable"
)
AmazonS3_node1697998973307.setFormat("csv")
AmazonS3_node1697998973307.writeFrame(ChangeSchema_node1700789432112)
job.commit()
