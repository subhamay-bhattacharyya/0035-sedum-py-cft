from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.integration import SF
from diagrams.programming.flowchart import Decision,StartEnd

# from diagrams.aws.database import ElastiCache, RDS
# from diagrams.aws.network import ELB
# from diagrams.aws.network import Route53

with Diagram("Call Center WorkFlow", show=False, direction="TB"):
    # dns = Route53("dns")
    # lb = ELB("lb")

    with Cluster("Step Function Lambdas"):
        step_function = SF("Step Function")
        step_function - [LambdaFunction("Open Case"),
                         LambdaFunction("Assign Case"),
                         LambdaFunction("Work on Case"),
                         LambdaFunction("Escalate Case"),
                         LambdaFunction("Close Case")]
        



