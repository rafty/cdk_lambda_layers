#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from stacks.lambda_layers_stack import CdkLambdaLayersStack

environment = cdk.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]),
)

app = cdk.App()

CdkLambdaLayersStack(app, "CdkLambdaLayersStack", env=environment)

app.synth()
