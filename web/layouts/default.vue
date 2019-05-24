<template>
  <v-app>
    <shiba-toolbar/>
    <v-content>
        <nuxt/>
    </v-content>
  </v-app>
</template>

<script>
  import ShibaToolbar from '@/components/shiba-toolbar'

  export default {
    components: {
      ShibaToolbar
    },
    head() {
      return {
        title: "Shiba"
      }
    }
  }
</script>
