<template>
  <v-app>
    <v-navigation-drawer absolute app clipped="false">
      <v-toolbar flat class="transparent">
        <v-list class="pa-3">
          <v-list-tile v-for="menu in menus" :key="menu.id" @click="">
            <v-list-tile-action>
              <v-icon color="primary">{{menu.icon}}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{menu.name}}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-toolbar>
    </v-navigation-drawer>
    <v-toolbar dark app fixed color="primary" clipped-left="true">
      <v-icon>rowing</v-icon>
      <v-toolbar-title>Peak</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-avatar color="info">
        <span class="headline">C</span>
      </v-avatar>
    </v-toolbar>
    <v-content>
      <v-container>
        <nuxt/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    data() {
      return {
        menus: [
          {icon: "room", name: "项目", id: "123123"},
          {icon: "room", name: "应用", id: "123123"},
          {icon: "room", name: "主机", id: "123123"},
          {icon: "rowing", name: "发布任务", id: "123123"},
          {icon: "phone", name: "用户", id: "12322123"},
          {icon: "phone", name: "角色", id: "123122123"},
        ]
      }
    }
  }
</script>
