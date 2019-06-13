<template>
  <div>{{projectKey}}项目用户</div>
</template>

<script>
  export default {
    layout: "project",
    head() {
      return {
        title: "项目成员"
      }
    },
    data() {
      return {
        projectKey: this.$route.params.key
      }
    }
  }
</script>
