<template>
  <v-card height="100%">
    <v-card-title style="height: 12%">
      <span class="headline font-weight-black">主机列表</span>
      <v-spacer/>
      <v-btn color="primary">同步主机</v-btn>
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
    head() {
      return {
        title: "主机"
      }
    },
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
