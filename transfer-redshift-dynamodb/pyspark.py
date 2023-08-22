import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
glue_context= GlueContext(SparkContext.getOrCreate())
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

# mention Redshift details here
redshift_connection_options = {  
    "url": "JDBC URL",
    "dbtable": "redshift-table-name",
    "redshiftTmpDir": args["TempDir"],
    "user": "redshift-namespace-admin-username",
    "password": "redshift-namespace-admin-password"
}

dfs = glue_context.create_dynamic_frame_from_options("redshift", redshift_connection_options)

# mention DynamoDB details here
glue_context.write_dynamic_frame_from_options(
    frame=dfs,
    connection_type="dynamodb",
    connection_options={
        "dynamodb.region": "table-region",
        "dynamodb.output.tableName": "table-name"
    }
)

job.commit()