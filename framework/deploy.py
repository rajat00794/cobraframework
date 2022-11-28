from typing import Optional, Dict


class DeploymentConfig:
    def __init__(self, deploymentutils: Optional[object] = None) -> None:
        if deploymentutils is not None:
            self.utils = deploymentutils

    def deployment_with_docker_template(self):
        template = self.utils.generate_deployment_template()
        return template

    def deploy(self, type: Dict[str, str]):
        if "type" in list(type.keys()):
            if type["type"] == "docker":
                print("==================Loading deployment config==================")
                template = self.utils.load_deployment_template()
                print("================== Generating files ==================")
                self.utils.generate_files(template)
                print("================== deploying application ==================")
                data = self.utils.run_deployment_commands()
                return dict(response=f"deployed docker app {data}")
            else:
                raise Exception("work in progress")

    def prepare_deployment(self, type: str):
        if type == "docker":
            return self.deployment_with_docker_template()
