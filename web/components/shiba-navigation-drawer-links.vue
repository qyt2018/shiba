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
            <div>sadfjklasdfjl</div>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat @click="addLinkFormVisible = false">取消</v-btn>
              <v-btn color="primary" flat @click="addLinkFormVisible = false">保存</v-btn>
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
              {{link.lable}}</a>
          </v-list-tile-title>
        </v-list-tile-content>
        <v-list-tile-action>
          <v-icon small>delete</v-icon>
        </v-list-tile-action>
      </v-list-tile>
    </v-list>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        links: [
          {id: 1, lable: "测试连接", url: "http://www.baidu.com"},
          {id: 2, lable: "测试连接1", url: "http://www.baidu.com"},
          {id: 3, lable: "测试连接2", url: "http://www.baidu.com"},
          {id: 4, lable: "测试连接3", url: "http://www.baidu.com"}
        ],
        addLinkFormVisible: false
      }
    }
  }
</script>
