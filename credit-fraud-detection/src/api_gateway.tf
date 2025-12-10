resource "aws_apigatewayv2_api" "fraud_api" {
  name          = "fraud-api"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                  = aws_apigatewayv2_api.fraud_api.id
  integration_type        = "AWS_PROXY"
  integration_uri         = aws_lambda_function.fraud_model.invoke_arn
}
