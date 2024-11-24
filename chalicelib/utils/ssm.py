import boto3


def get_firebase_credential(parameter: str) -> str:
    ssm = boto3.client("ssm")
    response = ssm.get_parameter(Name=parameter)

    return response["Parameter"]["Value"]
