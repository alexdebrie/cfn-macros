## DynamoDB Defaults macro

This directory contains a [CloudFormation macro](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) to add default properties to DynamoDB tables that use the macro.

For every DynamoDB table to which this macro is attached, it will

- Check the `BillingMode` property and set it to `PAY_PER_REQUEST` if not defined;

- Add default read and write capacity units of 1 if the `BillingMode` is `PROVISIONED` but the throughput is not given;

- Add a DynamoDB stream

For a full walkthrough on how and why to use this, check out [my blog post on CloudFormation macros](https://alexdebrie.com/posts/cloudformation-macros/).

## Usage

After cloning this directory, you can use this macro as follows:

1. Deploy and register the macro in your AWS account.

	Install the [Serverless Framework](https://github.com/serverless/serverless) to easily deploy Lambda functions.
	
	Then, run `serverless deploy` to deploy the macro and register it as `DynamoDBDefaults` in your AWS account.
	
2. Use the macro in your CloudFormation templates:

	Use the macro by adding a `Fn::Transform` property to a DynamoDB table resource in your CloudFormation template:
	
	```yml
	Resources:
	  MyNewTable:
	    Type: AWS::DynamoDB::Table
	    Properties:
	      TableName: 'MyNewTable'
	      KeySchema:
	        - AttributeName: key
	          KeyType: HASH
	      AttributeDefinitions:
	        - AttributeName: key
	          AttributeType: S
	      Fn::Transform: DynamoDBDefaults # <-- Macro
   ```
   
   There is a template provided in `template.yaml` that you can deploy with the following command:
   
   ```bash
   aws cloudformation deploy \
     --stack-name dynamodb-table-macro \
     --template-file template.yaml
   ```