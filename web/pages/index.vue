<template>
  <v-card height="100%">
    <v-card-title style="height: 12%">
      <span class="headline font-weight-black">本周发布</span>
    </v-card-title>
    <v-divider/>
    <v-card-text>

    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    head() {
      return {
        title: "主页"
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
