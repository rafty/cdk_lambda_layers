from aws_cdk import core as cdk
from _constructs.lambda_layer_construct import LambdaLayerConstruct
from _constructs.lambda_function_construct import LambdaFunctionConstruct


class CdkLambdaLayersStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # lambda layer
        layer_construct = LambdaLayerConstruct(
            scope=self,
            id='LambdaLayerConstruct',
            layer_version_name='Base')

        base_layer = layer_construct.lambda_layer(
            language='python',
            layer_code_path='src/layers/base'
        )

        # lambda function
        function_construct = LambdaFunctionConstruct(
            scope=self,
            id='LambdaFunctionConstruct',
            function_name='base_app')

        function_construct.lambda_function(
            handler='base_app.handler',
            function_path='src/lambda/base',
            lambda_layers=[base_layer]
        )

