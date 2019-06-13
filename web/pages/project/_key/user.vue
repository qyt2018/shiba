<template>
  <v-card height="100%">
    <v-card-title>
      <span class="title font-weight-black">项目成员</span>
    </v-card-title>
    <v-card-title>
      <v-container>
        <v-form>
          <v-layout justify-space-between>
            <v-flex offset-xs1 xs5>
              <v-autocomplete :items="userList" :rules="[v => !!v || '必填']" :search-input.sync="userSearch"
                              :loading="userSearchLoading" item-text="name" item-value="id" required label="用户"/>
            </v-flex>
            <v-flex xs2>
              <v-select item-text="name" item-value="key" :items="roles" label="角色">
              </v-select>
            </v-flex>
            <v-flex xs2>
              <v-btn color="primary">添加</v-btn>
            </v-flex>
          </v-layout>
        </v-form>
      </v-container>
    </v-card-title>
    <v-divider/>
    <v-card-text>
      <v-data-table>
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
        roles: [
          {key: "DEV", name: "开发"},
          {key: "TEST", name: "测试"},
          {key: "OPS", name: "运维"}
        ]
      }
    },
    mounted() {
      this.queryUserList()
    },
    methods: {
      queryUserList() {
        this.userSearchLoading = true;
        this.$axios.get("/api/user/").then(({data}) => {
          this.userList = data.result;
          this.userSearchLoading = false;
        })
      }
    }
  }
</script>
