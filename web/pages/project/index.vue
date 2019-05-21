<template>
  <div>项目列表
  <v-btn to="/project/ceshi">测试</v-btn></div>
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
