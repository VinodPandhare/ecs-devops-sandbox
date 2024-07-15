#!/usr/bin/env python3
import os
import sys

# Adjusting Python path to include ecs_devops_sandbox_cdk directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ecs_devops_sandbox_cdk')))

import aws_cdk as cdk
from ecs_devops_sandbox_cdk.ecs_devops_sandbox_cdk_stack import EcsDevopsSandboxCdkStack

app = cdk.App()
EcsDevopsSandboxCdkStack(app, "EcsDevopsSandboxCdkStack")

app.synth()
