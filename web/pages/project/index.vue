<template>
  <v-card height="100%">
    <v-card-title>
      <span class="headline font-weight-black">项目列表</span>
      <v-spacer/>
      <v-btn color="primary">创建项目</v-btn>
    </v-card-title>
    <v-divider/>
    <v-container fluid>
      <v-layout fill-height>
        <v-flex xs2>
          <v-btn to="/project/ceshi">测试</v-btn>
        </v-flex>
        <v-divider :vertical="true"/>
        <v-flex xs10>
          <v-btn to="/project/ceshi">测试</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>
  export default {
    data() {
      return {
        result: null
      }
    },
    mounted() {
      this.$axios.get("/api/project/").then(({data}) => {
        this.result = data;
      })
    }
  }
</script>
