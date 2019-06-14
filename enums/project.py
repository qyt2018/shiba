from enum import Enum


class ProjectRoleEnums(Enum):
    OWNER = '负责人'
    DEV = '开发'
    TEST = '测试'
    OPS = '运维'

    def __str__(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls[item].name
