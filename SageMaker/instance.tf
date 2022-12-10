resource "aws_sagemaker_notebook_instance" "notebookinstance" {
  name          = "primuslearningnotebook"
  role_arn      = "arn:aws:iam::274127640471:role/service-role/AmazonSageMaker-ExecutionRole-20220515T191615"
  instance_type = "ml.t2.medium"

  tags = {
    Name = "primuslearning_sagemaker_instance"
  }
}