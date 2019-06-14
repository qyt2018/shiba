<template>
  <v-card height="100%">
    <v-card-title  style="height: 12%">
      <span class="title font-weight-black">应用</span>
      <v-spacer/>
      <v-btn color="primary">创建应用</v-btn>
    </v-card-title>
    <v-divider/>
    <v-card-text>
      <v-data-table :items="[]">
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    layout: "project",
    head() {
      return {
        title: "应用"
      }
    },
    data() {
      return {
        projectKey: this.$route.params.key
      }
    }
  }
</script>
