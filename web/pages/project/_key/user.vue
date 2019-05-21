<template>
  <div>{{projectKey}}项目用户</div>
</template>

<script>
  export default {
    layout: "project",
    data() {
      return {
        projectKey: this.$route.params.key
      }
    }
  }
</script>
