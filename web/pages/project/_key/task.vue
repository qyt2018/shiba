<template>
  <div>{{projectKey}}项目发布任务</div>
</template>

<script>
  export default {
    layout: "project",
    head() {
      return {
        title: "发布任务"
      }
    },
    data() {
      return {
        projectKey: this.$route.params.key
      }
    }
  }
</script>
