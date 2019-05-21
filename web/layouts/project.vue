<template>
  <v-app>
    <v-navigation-drawer width="228" absolute app clipped>
      <v-toolbar flat>
        <v-list>
          <v-list-tile>
            <v-list-tile-title class="title">
              {{ project.name }}
            </v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-toolbar>
      <v-divider></v-divider>
      <v-list dense class="pa-3">
        <v-list-tile v-for="menu in menus" :key="menu.id" @click="">
          <v-list-tile-action>
            <v-icon color="primary">{{menu.icon}}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title style="font-weight: bold;">{{menu.name}}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
      <v-list-tile>
        <v-list-tile-title style="color: grey;" class="body-1 font-weight-bold">
          相关连接
        </v-list-tile-title>
        <v-list-tile-action style="justify-content: flex-end">
          <v-btn small icon fab>
            <v-icon>add</v-icon>
          </v-btn>
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
    </v-navigation-drawer>

    <shiba-toolbar/>
    <v-content>
      <v-container>
        <nuxt/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import ShibaToolbar from '@/components/shiba-toolbar'

  export default {
    components: {
      ShibaToolbar
    },
    head() {
      return {
        title: "Shiba"
      }
    },
    data() {
      return {
        menus: [
          {icon: "rowing", name: "发布任务", id: "123123"},
          {icon: "apps", name: "应用", id: "12321222123"},
          {icon: "computer", name: "主机", id: "123123323223"},
          {icon: "group", name: "成员", id: "12322123"}
        ],
        links: [
          {id: 1, lable: "测试连接", url: "http://www.baidu.com"},
          {id: 2, lable: "测试连接1", url: "http://www.baidu.com"},
          {id: 3, lable: "测试连接2", url: "http://www.baidu.com"},
          {id: 4, lable: "测试连接3", url: "http://www.baidu.com"}
        ],
        project: {
          name: "EV流程管理系统"
        }
      }
    }
  }
</script>
