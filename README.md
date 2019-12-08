# CreatedBy Tag Automation using Lambda 

With CloudWatch Events and Lambda, we can tag new instances of EC2 and RDS with a tag that can tell who created this feature.

![](diagram.jpeg)

# First steps
* Cloudformation file and Python script are ready to run except:
    - Enter the correct Role for Lambda execution;
    - Update S3Bucket and S3Key to the values of your environment.
 
# Add features for tagging
* To add a new feature to monitoring and tagging, follow these steps:
    - Include the required eventName and eventSource in the CloudWatch Event;
    - Create a Scroll to the createdby-tag.py script to access the required resources.