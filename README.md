# Risuku
Taking counterparties news from Bloomberb News and Google News. Feed it into AWS Comprehension to perform risk analysis to determine performance which can be taking as a nudge to fund manager.

## AWS Setup
How to set up AWS account and using the AWS API. The SDK we are using is Boto3 - which is for Python. Sing up to AWS - you will have access to free tier. In my case I am using AWS Educate.
```pip install Boto3```

### Requirements

* Create an user account via IAM
This will provides the following for Boto3 so you can create an instance of a client to use different AWS services:
 - Access Key
 - Secrey Key
 - Roles and Policy. You can create roles which will provides access to the group. Restrictions to different services. 
* Download and Install AWS CLI 2
The CLI allows you to call AWS services. Additionaly allows you to set up configuration.
Following are useful commands:
```aws configure```
```aws which```

### Django

```python manage.py runserver 8080```