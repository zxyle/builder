import os
import zipfile

from requests import Session

session = Session()


class Starter:
    # start.spring.io start.springboot.io
    hostname = "https://start.springboot.io"
    zip_location = ""

    def __init__(self, metadata):
        self.group_id = metadata.get("group")
        self.artifact_id = metadata.get("artifact")

        info = self.get_info()
        latest_version = info.get("bootVersion").get("default")

        self.params = {
            # gradle-project maven-project
            "type": "maven-project",
            # java kotlin groovy
            "language": "java",
            "bootVersion": latest_version,
            "baseDir": self.artifact_id,
            "groupId": self.group_id,
            "artifactId": self.artifact_id,
            "name": self.artifact_id,
            "description": "Demo project for Spring Boot",
            "packageName": f"{self.group_id}.{self.artifact_id}",
            "packaging": "jar",
            # 16 11 1.8
            "javaVersion": "1.8",
            "dependencies": "devtools,lombok,configuration-processor,web,mysql,actuator,validation",
        }
        metadata.update({
            "libs": self.params.get("dependencies"),
            "packaging": self.params.get("packaging"),
            "description": self.params.get("description"),
            "bootVersion": self.params.get("bootVersion").replace(".RELEASE", ""),
        })

        self.zip_location = f"{self.artifact_id}.zip"

    def get_info(self):
        url = f"{self.hostname}/metadata/client"
        resp = session.get(url)
        return resp.json()

    def download(self):
        url = f"{self.hostname}/starter.zip"
        resp = session.get(url, params=self.params)
        with open(self.zip_location, "wb") as f:
            f.write(resp.content)

    def cleanup(self):
        if os.path.exists(self.zip_location):
            os.remove(self.zip_location)

    def unzip(self, dst_dir):
        with zipfile.ZipFile(self.zip_location, 'r') as fz:
            for file in fz.namelist():
                fz.extract(file, dst_dir)

    def run(self):
        pass
