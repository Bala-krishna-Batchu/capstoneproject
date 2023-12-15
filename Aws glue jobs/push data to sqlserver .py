import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1702077396116 = glueContext.create_dynamic_frame.from_catalog(
    database="airqdatabase",
    table_name="aws-glue-healthcare-county-transformed-table",
    transformation_ctx="AWSGlueDataCatalog_node1702077396116",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1702077412601 = glueContext.create_dynamic_frame.from_catalog(
    database="airqdatabase",
    table_name="aws-glue-openaqtable",
    transformation_ctx="AWSGlueDataCatalog_node1702077412601",
)

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1702077741261 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1702077396116,
    mappings=[
        ("county", "string", "right_county", "string"),
        ("year", "string", "right_year", "string"),
        ("month", "string", "right_month", "string"),
        ("day", "string", "right_day", "string"),
        ("date", "string", "right_date", "string"),
        ("asthma measure", "string", "right_asthma measure", "string"),
        ("comparison", "string", "right_comparison", "string"),
        ("group", "string", "right_group", "string"),
        ("county count", "string", "right_county count", "string"),
        ("county rate", "string", "right_county rate", "string"),
        ("california count", "string", "right_california count", "string"),
        ("california rate", "string", "right_california rate", "string"),
        ("death_count_location", "string", "right_death_count_location", "string"),
    ],
    transformation_ctx="RenamedkeysforJoin_node1702077741261",
)

# Script generated for node Join
AWSGlueDataCatalog_node1702077412601DF = AWSGlueDataCatalog_node1702077412601.toDF()
RenamedkeysforJoin_node1702077741261DF = RenamedkeysforJoin_node1702077741261.toDF()
Join_node1702077416194 = DynamicFrame.fromDF(
    AWSGlueDataCatalog_node1702077412601DF.join(
        RenamedkeysforJoin_node1702077741261DF,
        (
            AWSGlueDataCatalog_node1702077412601DF["country"]
            == RenamedkeysforJoin_node1702077741261DF["right_county"]
        ),
        "outer",
    ),
    glueContext,
    "Join_node1702077416194",
)

# Script generated for node Microsoft SQL Server
MicrosoftSQLServer_node1702077878661 = glueContext.write_dynamic_frame.from_catalog(
    frame=Join_node1702077416194,
    database="airqdatabase",
    table_name="aws-glue-openaqtable",
    transformation_ctx="MicrosoftSQLServer_node1702077878661",
)

# Script generated for node Amazon S3
AmazonS3_node1702077699226 = glueContext.getSink(
    path="s3://aws-glue-openaq-county-transformed",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1702077699226",
)
AmazonS3_node1702077699226.setCatalogInfo(
    catalogDatabase="airqdatabase", catalogTableName="table for ssms"
)
AmazonS3_node1702077699226.setFormat("csv")
AmazonS3_node1702077699226.writeFrame(Join_node1702077416194)
job.commit()
