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
        <v-icon right>keyboard_arrow_down</v-icon>
      </v-btn>
      <v-btn flat to="/project">项目
        <v-icon right>keyboard_arrow_down</v-icon>
      </v-btn>
      <v-btn flat to="/user">用户
        <v-icon right>keyboard_arrow_down</v-icon>
      </v-btn>
    </v-toolbar-items>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn flat>
        <v-avatar @click="" size="30" color="indigo">
          <v-icon dark>account_circle</v-icon>
        </v-avatar>
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
  export default {}
</script>
