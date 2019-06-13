<template>
  <v-card height="100%">
    <v-card-title>
      <span class="title font-weight-black">应用</span>
    </v-card-title>
    <v-divider/>
    <v-card-text>
      <v-data-table>
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
