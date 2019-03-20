## Python-style formating macro

This directory contains a [CloudFormation macro](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) to add Python-style string formating to your CloudFormation template.

With it, you'll be able to do formatting as follows:

```yml
Parameters:
  stage:
    Type: String
    Default: dev
    AllowedValues:
      - dev
      - staging
      - prod
Resources:
  MySNSTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: "MyTopic-{stage}" # <-- Python templating
Transform:
  - VariableSubstitution
```

For a full walkthrough on how and why to use this, check out [my blog post on CloudFormation macros](https://alexdebrie.com/posts/cloudformation-macros/).

## Usage

After cloning this directory, you can use this macro as follows:

1. Deploy and register the macro in your AWS account.

	Install the [Serverless Framework](https://github.com/serverless/serverless) to easily deploy Lambda functions.
	
	Then, run `serverless deploy` to deploy the macro and register it as `VariableSubstitution` in your AWS account.
	
2. Use the macro in your CloudFormation templates:

	Use the macro by adding a `Transform` property to your CloudFormation template:
	
	```yml
	Resources:
	  MySNSTopic:
	    Type: AWS::SNS::Topic
	    Properties:
	      TopicName: "MyTopic-{stage}" # <-- Python templating
	Transform:
	  - VariableSubstitution
	```
	
	   There is a template provided in `template.yaml` that you can deploy with the following command:
   
   ```bash
   aws cloudformation deploy \
     --stack-name sns-topic-variables \
     --template-file template.yaml
   ```