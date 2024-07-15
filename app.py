#!/usr/bin/env python3
import os

import aws_cdk as cdk
from ecs_devops_sandbox_cdk.ecs_devops_sandbox_cdk_stack import EcsDevopsSandboxCdkStack

app = cdk.App()
EcsDevopsSandboxCdkStack(app, "EcsDevopsSandboxCdkStack")

app.synth()
