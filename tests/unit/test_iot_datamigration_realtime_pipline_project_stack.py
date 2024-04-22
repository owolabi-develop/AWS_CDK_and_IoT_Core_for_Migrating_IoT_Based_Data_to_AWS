import aws_cdk as core
import aws_cdk.assertions as assertions

from iot_datamigration_realtime_pipline_project.iot_datamigration_realtime_pipline_project_stack import IotDatamigrationRealtimePiplineProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in iot_datamigration_realtime_pipline_project/iot_datamigration_realtime_pipline_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IotDatamigrationRealtimePiplineProjectStack(app, "iot-datamigration-realtime-pipline-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
