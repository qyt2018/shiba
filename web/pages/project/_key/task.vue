<template>
  <div>{{projectKey}}项目发布任务</div>
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
