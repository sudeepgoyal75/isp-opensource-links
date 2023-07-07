# SSM

aws ssm start-session --target "i-xxxxxxxx" --document-name AWS-StartPortForwardingSession --parameters "portNumber=443"

# AWS modules

terraform-aws-modules/vpc/aws

# Cognito Document

https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html
https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/update-user-pool-client.html
--allowed-o-auth-flows-user-pool-client to be true for oauth
