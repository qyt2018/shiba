<template>
  <v-card height="100%">
    <!--创建用户-->
    <v-dialog max-width="500px" v-model="createUserDialogVisible">
      <v-card>
        <v-card-title class="title">
          添加用户
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-form ref="form" lazy-validation>
              <v-text-field :rules="[v => !!v || '姓名必填']" required v-model="form.name" label="姓名"/>
              <v-text-field :rules="[v => !!v || '用户名必填']" required v-model="form.username" label="用户名"/>
              <v-text-field :rules="[v => !!v || '密码必填']" type="password" required v-model="form.password" label="密码"/>
              <v-switch color="primary" label="管理员" v-model="form.is_admin"/>
            </v-form>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn flat color="grey" @click="closeUserDialog">取消</v-btn>
          <v-btn flat color="info" @click="createUser">提交</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-card-title style="height: 12%">
      <span class="headline font-weight-black">用户列表</span>
      <v-spacer/>
      <v-btn color="primary" @click="createUserDialogVisible=true">添加用户</v-btn>
    </v-card-title>
    <v-divider/>
    <v-card-text>
      <v-data-table :items="result" :headers="headers">
        <template v-slot:items="props">
          <td>{{props.item.name}}</td>
          <td>{{props.item.username}}</td>
          <td>
            <input type="checkbox" disabled v-model="props.item.is_admin"/>
          </td>
          <td>
            <v-btn small color="error" @click="deleteUser(props.item.id)" flat>删除</v-btn>
          </td>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    head() {
      return {
        title: "用户"
      }
    },
    data() {
      return {
        result: [],
        headers: [
          {"text": "姓名", "value": "name"},
          {"text": "用户名", "value": "username"},
          {"text": "管理员", "value": "is_admin"},
          {"text": "操作", "value": "action"},
        ],
        form: {
          name: null,
          username: null,
          password: null,
          is_admin: false
        },
        createUserDialogVisible: false
      }
    },
    mounted() {
      this.queryUserList()
    },
    methods: {
      queryUserList() {
        this.$axios.get("/api/user/").then(({data}) => {
          this.result = data.result;
        })
      },
      createUser() {
        if (this.$refs.form.validate()) {
          this.$axios.post("/api/user/create", this.form).then(({data}) => {
            this.closeUserDialog();
          })
        }
      },
      deleteUser(userId) {
        this.$confirm('确定删除吗？').then(res => {
          if (res) {
            this.$axios.post(`/api/user/${userId}/delete`, this.form).then(({data}) => {
              this.$toast.success(data.result);
              this.closeUserDialog();
            })
          }
        })
      },
      closeUserDialog() {
        this.$refs.form.reset();
        this.queryUserList();
        this.createUserDialogVisible = false;
      }
    }
  }
</script>
