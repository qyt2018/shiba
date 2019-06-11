### user
```
id
name
username
password
is_admin
token
```
### project
``` yaml
id
name
owner
jira_project
external_links: {
  name
  url
}
users: {
  user
  role_key
}
```
### app
```
id
name
project
git_uri
git_user
git_passwd
jenkins_job
```
### task
```
id
name
type
state
project
apps: []
release_time
real_release_time
remark
jira_version
create_user
create_time
```