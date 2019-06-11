import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../"))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
NUXT_STATIC_DIR = os.path.join(TEMPLATE_DIR, "_nuxt")
STATIC_DIR = os.path.join(BASE_DIR, "static")
PORT = 8001
HOST = '0.0.0.0'
DEBUG = False
MOTOR_URI = "mongodb://shiba:shiba@127.0.0.1:27017/shiba"
LOGO = None
JENKINS_URL = ""
JENKINS_USER = ""
JENKINS_PASSWD = ""
JIRA_URL = ""
JIRA_USER = ""
JIRA_PASSWD = ""
