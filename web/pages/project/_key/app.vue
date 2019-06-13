<template>
  <div>{{projectKey}}项目APP</div>
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
