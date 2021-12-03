from aws_cdk import CfnOutput
from constructs import Construct
from aws_cdk import aws_lambda
from aws_cdk import Tags


class LambdaFunctionConstruct(Construct):

    def __init__(self, scope: Construct, id: str, function_name: str) -> None:
        super().__init__(scope, id)
        self._function_name = function_name
        self._construct_id = id
        self._function_arn = None

    def lambda_function(self,
                        handler: str,
                        function_path: str,
                        description: str = None,
                        lambda_layers: list = None
                        ) -> aws_lambda.Function:

        _function = aws_lambda.Function(
            scope=self,
            id=f'LambdaFunction-{self._function_name}',
            function_name=self._function_name,
            description=description,
            handler=handler,
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            # code=aws_lambda.Code.asset(function_path),
            code=aws_lambda.Code.from_asset(function_path),
            layers=lambda_layers
        )

        self._function_arn = _function.function_arn

        Tags.of(_function).add('FunctionName', self._function_name)

        CfnOutput(
            scope=self,
            id='lambda_function_name',
            value=_function.function_name
        )

        CfnOutput(
            scope=self,
            id='lambda_function_arn',
            value=_function.function_arn
        )

        return _function

    @property
    def function_arn(self):
        return self._function_arn
