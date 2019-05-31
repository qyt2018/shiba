<template>

  <v-toolbar dense dark app fixed color="primary" :clipped-left="true">
    <v-toolbar-items style="width: 203px;">
      <v-btn block :ripple="false" flat style="margin-right: 24px;">
        <v-icon>rowing</v-icon>
        <v-toolbar-title>Shiba</v-toolbar-title>
      </v-btn>
    </v-toolbar-items>
    <v-toolbar-items>
      <v-btn flat to="/">主页
        <v-icon right>adjust</v-icon>
      </v-btn>
      <v-btn flat to="/project">项目
        <v-icon right>adjust</v-icon>
      </v-btn>
      <v-btn flat v-if="$auth.hasScope('admin')" to="/host">主机
        <v-icon right>adjust</v-icon>
      </v-btn>
      <v-btn flat v-if="$auth.hasScope('admin')" to="/user">用户
        <v-icon right>adjust</v-icon>
      </v-btn>
    </v-toolbar-items>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" flat>
            <v-icon left dark>account_circle</v-icon>
            {{$auth.user.name}}
            <v-icon right>keyboard_arrow_down</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-tile @click="logout">
            <v-list-tile-title>登出</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
  export default {
    methods: {
      logout() {
        this.$auth.logout();
      }
    }
  }
</script>
