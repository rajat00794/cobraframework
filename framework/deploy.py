from typing import Optional


class DeploymentConfig:
    def __init__(self, deploymentutils: Optional[object] = None) -> None:
        if deploymentutils is not None:
            self.utils = deploymentutils

    def deployment_with_docker(self):
        dtype = input(
            "Deployment type:ex:docker:",
        )
        dhost = input(
            "Deployment host:ex:aws:",
        )
        docker_config = ""
        pass
