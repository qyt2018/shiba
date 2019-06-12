<template>
  <v-dialog v-model="visible" persistent max-width="500">
    <v-card>
      <v-card-title class="title">创建项目</v-card-title>
      <v-card-text>
        <v-container>
          <v-form ref="form" lazy-validation>
            <v-text-field :rules="[v => !!v || '必填']" required v-model="form.name" label="名称"/>
            <v-text-field :rules="[v => !!v || '必填']" required v-model="form.key" label="关键字"/>
            <v-autocomplete :items="userList" :rules="[v => !!v || '必填']" :search-input.sync="userSearch"
                            :loading="userSearchLoading" item-text="name" item-value="id" required v-model="form.owner"
                            label="负责人"/>
          </v-form>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn flat color="grey" @click="close">取消</v-btn>
        <v-btn flat color="info" @click="save">提交</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
  export default {
    name: "ProjectCreateDialog",
    data() {
      return {
        form: {},
        userList: [],
        userSearch: null,
        userSearchLoading: false
      }
    },
    watch: {
      'form.key': function (newVal, oldVal) {
        if (newVal) {
          this.form.key = newVal.toUpperCase();
        }
      },
      userSearch(val) {
        /*
        todo 分页后端查询搜索
         */
        if (this.userList.length <= 0) {
          val && this.queryUserList(val)
        }
      }
    },
    props: {
      visible: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      close() {
        this.$refs.form.reset();
        this.userList = [];
        this.$emit('close');
      },
      queryUserList(val) {
        this.userSearchLoading = false;
        this.$axios.get("/api/user/").then(({data}) => {
          this.userList = data.result;
        })
      },
      save() {
        if (this.$refs.form.validate()) {
          this.$axios.post("/api/project/create", this.form).then(({data}) => {
            this.$toast.success(`创建成功：${data.result}`);
            this.close();
          })
        }
      }
    }
  }
</script>

<style scoped>

</style>
