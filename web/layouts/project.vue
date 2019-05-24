<template>
  <v-app>
    <shiba-navigation-drawer/>
    <shiba-toolbar/>
    <v-content>
        <nuxt/>
    </v-content>
  </v-app>
</template>

<script>
  import ShibaToolbar from '@/components/shiba-toolbar';
  import ShibaNavigationDrawer from '@/components/shiba-navigation-drawer';

  export default {
    components: {
      ShibaToolbar,
      ShibaNavigationDrawer
    },
    head() {
      return {
        title: "Shiba"
      }
    },
    data() {
      return {}
    }
  }
</script>
