<template>
  <div>{{projectKey}}项目APP</div>
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
