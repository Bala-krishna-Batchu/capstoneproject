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

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1700727154635 = glueContext.create_dynamic_frame.from_catalog(
    database="airqdatabase",
    table_name="aws-glue-openaqtable",
    transformation_ctx="AWSGlueDataCatalog_node1700727154635",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1700727403052 = DynamicFrame.fromDF(
    AWSGlueDataCatalog_node1700727154635.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1700727403052",
)

job.commit()
