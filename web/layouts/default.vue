<template>
  <v-app>
    <shiba-toolbar/>
    <v-content>
      <v-container>
        <nuxt/>
      </v-container>
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
