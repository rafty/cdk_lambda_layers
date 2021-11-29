from aws_cdk import core as cdk
from aws_cdk import aws_lambda


class LambdaLayerConstruct(cdk.Construct):
    def __init__(self,
                 scope: cdk.Construct,
                 id: str,
                 layer_version_name: str,
                 ) -> None:
        super().__init__(scope, id)

        self._layer_version_name = layer_version_name

    def lambda_layer(
            self,
            language: str,
            layer_code_path: str) -> aws_lambda.LayerVersion:

        lang_path = language
        commands = [
            '/bin/bash',
            '-c',
            f"""
            pip install -r requirements.txt -t /asset-output/{lang_path} &&
            cp -au . /asset-output/{lang_path}
            """
        ]

        bundling = cdk.BundlingOptions(
            image=aws_lambda.Runtime.PYTHON_3_8.bundling_docker_image,
            command=commands
        )

        code = aws_lambda.Code.from_asset(
            path=layer_code_path,
            bundling=bundling
        )

        layer = aws_lambda.LayerVersion(
            scope=self,
            id='LambdaConstructLayerVersion',
            layer_version_name=self._layer_version_name,
            code=code
        )
        return layer
