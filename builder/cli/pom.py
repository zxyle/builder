GROUP = "org.springframework.boot"


class Base:
    group_id = GROUP
    artifact_id = None

    def __init__(self, group_id, artifact_id):
        self.group_id = group_id
        self.artifact_id = artifact_id


class Dependency(Base):
    def __init__(self, group_id, artifact_id, version=None, scope=None, optional=None):
        super(Dependency, self).__init__(group_id, artifact_id)
        self.version = version
        self.scope = scope
        self.optional = optional
        self.exclusions = []
        self.comment = ""

    def add_exclude(self, group_id, artifact_id):
        exclusion = Exclusion(group_id, artifact_id)
        self.exclusions.append(exclusion)

    def add_exclusions(self, exclusions):
        self.exclusions.extend(exclusions)

    def __eq__(self, other):
        return self.group_id == other.group_id and \
               self.artifact_id == other.artifact_id


class Property:
    def __init__(self, element, value):
        self.element = element
        self.value = value


class Exclusion(Base):
    def __init__(self, group_id, artifact_id):
        super().__init__(group_id, artifact_id)


class Plugin(Base):
    pass


class Dependencies:
    dependencies = set()

    def add(self):
        pass


# spring boot dependency
web_exclusions = [
    Exclusion(GROUP, "spring-boot-starter-tomcat"),
    Exclusion(GROUP, "spring-boot-starter-logging"),
]

web_stater = Dependency(GROUP, "spring-boot-starter-web")
web_stater.add_exclusions(web_exclusions)

dependencies = [
    Dependency(GROUP, "spring-boot-starter-actuator"),
    Dependency(GROUP, "spring-boot-starter-validation"),
    web_stater,
    Dependency(GROUP, "spring-boot-starter-undertow"),
    # Dependency(GROUP, "spring-boot-starter-log4j2"),
    # Dependency(GROUP, "spring-boot-starter-mail"),
    # Dependency(GROUP, "spring-boot-starter-quartz"),
    Dependency(GROUP, "spring-boot-starter-cache"),
    Dependency(GROUP, "spring-boot-starter-freemarker"),
    Dependency(GROUP, "spring-boot-starter-jdbc"),
    Dependency(GROUP, "spring-boot-starter-test", scope="test"),
    # Dependency(GROUP, "spring-boot-starter-security"),
    Dependency(GROUP, "spring-boot-starter-data-redis"),
    Dependency(GROUP, "spring-session-data-redis"),
    Dependency(GROUP, "spring-boot-devtools", scope="runtime", optional="true"),
    Dependency(GROUP, "spring-boot-configuration-processor", optional="true"),
    Dependency("mysql", "mysql-connector-java", scope="runtime"),
    Dependency("org.projectlombok", "lombok", optional="true"),

    Dependency("com.baomidou", "mybatis-plus-boot-starter", version="3.2.0"),
    Dependency("com.baomidou", "mybatis-plus-generator", version="3.4.1"),
    Dependency("com.github.ben-manes.caffeine", "caffeine"),

    # Dependency("io.springfox", "springfox-swagger2", version="2.9.2"),
    # Dependency("io.springfox", "springfox-swagger-ui", version="2.9.2"),
    Dependency("com.github.xiaoymin", "knife4j-spring-boot-starter", version="3.0.2"),

    # Dependency("com.google.code.gson", "gson"),
    # Dependency("com.alibaba", "fastjson", version="1.2.74"),
    Dependency("cn.hutool", "hutool-all", version="5.6.1"),
    Dependency("p6spy", "p6spy", version="3.9.1"),
    Dependency("org.apache.commons", "commons-lang3"),
    Dependency("commons-io", "commons-io", version="2.8.0"),
    Dependency("org.apache.commons", "commons-pool2"),
    Dependency("org.apache.commons", "commons-collections4", version="4.4"),
    Dependency("com.auth0", "java-jwt", version="3.4.0"),
    Dependency("org.hashids", "hashids", version="1.0.3"),
]

properties = [
    Property("project.build.sourceEncoding", "UTF-8"),
    Property("argLine", "-Dfile.encoding=UTF-8"),
]
