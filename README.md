# CreatedBy Tag Automation using Lambda 

With CloudWatch Events and Lambda, we can tag new EC2 and RDS instances launches with a tag that can tell who create this resource.

![](diagram.jpeg)

# First steps
*   The Cloudformation file and Python script are ready to run except for:
    -   Insert the correct Role for Lambda execution;
    -   Updated the S3Bucket and S3Key to values of your environment;
 
# Add resources for tagging
   * To add no new resource to monitoring and tag, following this steps:
        -  Include in eventName and eventSource required in CloudWatch Event
        -  Create a function in createdby-tag.py to treat required resource