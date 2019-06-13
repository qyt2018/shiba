<template>
  <div>
    <v-list-tile>
      <v-list-tile-title style="color: grey;" class="body-1 font-weight-bold">
        相关连接
      </v-list-tile-title>
      <v-list-tile-action style="justify-content: flex-end">
        <v-menu
          v-model="addLinkFormVisible"
          :close-on-content-click="false"
          :nudge-width="200"
          offset-x
        >
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" small icon fab>
              <v-icon>add</v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="title">添加链接</span>
            </v-card-title>
            <v-card-text>
              <v-form ref="form" class="ml-1 mr-1">
                <v-text-field :rules="[v => !!v || '必填']" required v-model="form.name" label="名称"/>
                <v-text-field :rules="[v => !!v || '必填']" required v-model="form.url" label="URL"/>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat @click="addLinkFormVisible = false">取消</v-btn>
              <v-btn color="primary" flat @click="addProjectLink">保存</v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-list-tile-action>
    </v-list-tile>
    <v-divider></v-divider>
    <v-list dense class="pa-3">
      <v-list-tile v-for="link in links" :key="link.id" @click="">
        <v-list-tile-content>
          <v-list-tile-title class="caption font-weight-medium font-italic">
            <a target="_blank" :href="link.url" style="color: #000;">
              <v-icon left>link</v-icon>
              {{link.name}}</a>
          </v-list-tile-title>
        </v-list-tile-content>
        <v-list-tile-action>
          <v-icon @click="deleteProjectLink(link.id)" small>delete</v-icon>
        </v-list-tile-action>
      </v-list-tile>
    </v-list>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        links: [],
        addLinkFormVisible: false,
        projectKey: this.$route.params.key,
        form: {}
      }
    },
    watch: {
      projectLinks(val) {
        this.links = val;
      }
    },
    props: {
      projectLinks: {
        type: Array
      }
    },
    methods: {
      addProjectLink() {
        if (this.$refs.form.validate()) {
          this.$axios.post(`/api/project/${this.projectKey}/add_link`, this.form).then(({data}) => {
            this.links = data.result;
            this.$toast.success(`修改成功`);
            this.$refs.form.reset();
            this.addLinkFormVisible = false;
          })
        }
      },
      deleteProjectLink(id) {
        this.$confirm('确定删除吗？').then(res => {
          if (res) {
            this.$axios.post(`/api/project/${this.projectKey}/delete_link`, {'link_id': id}).then(({data}) => {
              this.links = data.result;
              this.$toast.success(`删除成功`);
            })
          }
        })
      }
    }
  }
</script>
