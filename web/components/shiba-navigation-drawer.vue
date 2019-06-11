<template>
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
      <v-list-tile exact :to="menu.url" v-for="menu in menus" :key="menu.id" @click="">
        <v-list-tile-action>
          <v-icon>{{menu.icon}}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title style="font-weight: bold;">{{menu.name}}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
    <shiba-navigation-drawer-links/>
  </v-navigation-drawer>
</template>

<script>
  import ShibaNavigationDrawerLinks from '@/components/shiba-navigation-drawer-links';

  export default {
    components: {
      ShibaNavigationDrawerLinks
    },
    data() {
      return {
        menus: [
          {icon: "dashboard", name: "主页", id: "12312323", url: `/project/${this.$route.params.key}`},
          {icon: "rowing", name: "发布任务", id: "123123", url: `/project/${this.$route.params.key}/task`},
          {icon: "apps", name: "应用", id: "12321222123", url: `/project/${this.$route.params.key}/app`},
          {icon: "group", name: "成员", id: "12322123", url: `/project/${this.$route.params.key}/user`}
        ],
        project: {
          name: "EV流程管理系统"
        }
      }
    }
  }
</script>
