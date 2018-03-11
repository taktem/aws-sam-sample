# aws-sam-sample

# Local test
```bash
sam local start-api
```

# Deploy
```bash
sam package --template-file template.yml --s3-bucket [your s3 bucket name] --output-template-file package.yml --profile [your profile name]
sam deploy --template-file package.yml --stack-name [your stack name] --capabilities CAPABILITY_IAM  --profile [your profile name]
```
