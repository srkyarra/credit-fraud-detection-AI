resource "aws_lambda_function" "fraud_model" {
  function_name = "fraud_detection_lambda"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.10"
  role          = aws_iam_role.lambda_role.arn
  filename      = "../package/lambda.zip"

  environment {
    variables = {
      MODEL_BUCKET = "fraud-model-bucket"
      MODEL_KEY    = "fraud_model.pkl"
    }
  }
}
