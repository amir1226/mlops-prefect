from time import sleep
from prefect_gcp import GcpCredentials, GcsBucket

credentials_path = ""

def create_gcp_creds_block():
    gcp_creds_obj = GcpCredentials(
        service_account_file=credentials_path
    )
    gcp_creds_obj.save(name="my-gcp-creds", overwrite=True)


def create_cs_bucket_block():
    gcp_cred = GcpCredentials.load("my-gcp-creds")
    gcp_bucket_obj = GcsBucket(
        bucket="prefect-example-1", gcp_credentials=gcp_cred
    )
    gcp_bucket_obj.save(name="gcs-bucket-example", overwrite=True)


if __name__ == "__main__":
    create_gcp_creds_block()
    sleep(5)
    create_cs_bucket_block()
