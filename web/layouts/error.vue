<template>
  <v-container>
    <h1 v-if="error.statusCode === 404">页面不存在</h1>
    <h1 v-else>应用发生错误异常</h1>
    <span>{{totalTime}}秒后返回<nuxt-link to="/">首 页</nuxt-link></span>
  </v-container>
</template>

<script>
  export default {
    props: ['error'],
    layout: 'blank',
    data() {
      return {
        totalTime: 3,
        clock: null
      }
    },
    mounted() {
      this.clock = window.setInterval(() => {
        this.totalTime--;
        if (this.totalTime <= 0) {
          window.clearInterval(this.clock);
          this.$router.push({path: "/"});
        }
      }, 1000)
    },
    destroyed() {
      window.clearInterval(this.clock);
    }
  }
</script>
