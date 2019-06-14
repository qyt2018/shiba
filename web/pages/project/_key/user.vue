<template>
  <v-card height="100%">
    <v-card-title>
      <span class="title font-weight-black">项目成员</span>
    </v-card-title>
    <v-card-title>
      <v-container>
        <v-form ref="form">
          <v-layout justify-space-between>
            <v-flex offset-xs1 xs5>
              <v-autocomplete :items="userList" :rules="[v => !!v || '必填']" :search-input.sync="userSearch"
                              :loading="userSearchLoading" v-model="form.user" item-text="name" item-value="id" required
                              label="用户"/>
            </v-flex>
            <v-flex xs2>
              <v-select item-text="name" v-model="form.role_key" item-value="key" :items="roles" label="角色">
              </v-select>
            </v-flex>
            <v-flex xs2>
              <v-btn color="primary" @click="addUser">添加</v-btn>
            </v-flex>
          </v-layout>
        </v-form>
      </v-container>
    </v-card-title>
    <v-divider/>
    <v-card-text>
      <v-data-table :headers="headers" :items="projectUserList">
        <template v-slot:items="props">
          <td>{{props.index +1}}</td>
          <td>{{props.item.role_name}}</td>
          <td>{{props.item.user_detail.name}}</td>
          <td>
            <v-btn small color="error" v-if="props.item.role_key!=='OWNER'" @click="deleteProjectUser(props.item.id)"
                   flat>
              删除
            </v-btn>
          </td>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    layout: "project",
    head() {
      return {
        title: "项目成员"
      }
    },
    data() {
      return {
        projectKey: this.$route.params.key,
        userList: [],
        userSearchLoading: false,
        userSearch: null,
        projectUserList: [],
        form: {},
        roles: [
          {key: "DEV", name: "开发"},
          {key: "TEST", name: "测试"},
          {key: "OPS", name: "运维"}
        ],
        headers: [
          {text: 'ID', value: 'id'},
          {text: '角色', value: 'role_key'},
          {text: '用户', value: 'user'},
          {text: '操作', sortable: false, value: 'action'}
        ]
      }
    },
    mounted() {
      this.getProjectUsers();
      this.queryUserList()
    },
    methods: {
      queryUserList() {
        this.userSearchLoading = true;
        this.$axios.get("/api/user/").then(({data}) => {
          this.userList = data.result;
          this.userSearchLoading = false;
        })
      },
      getProjectUsers() {
        this.$axios.get(`/api/project/${this.projectKey}/user/`).then(({data}) => {
          this.projectUserList = data.result;
        })
      },
      deleteProjectUser(id) {
        this.$confirm('确定删除吗？').then(res => {
          if (res) {
            this.$axios.post(`/api/project/${this.projectKey}/delete_user/`, {'row_id': id}).then(({data}) => {
              this.projectUserList = data.result;
              this.$toast.success(`删除成功`);
            })
          }
        })
      },
      addUser() {
        if (this.$refs.form.validate()) {
          this.$axios.post(`/api/project/${this.projectKey}/add_user/`, this.form).then(({data}) => {
            this.$toast.success(`添加成功`);
            this.$refs.form.reset();
            this.getProjectUsers();
          })
        }
      }
    }
  }
</script>
