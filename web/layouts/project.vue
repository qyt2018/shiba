<template>
  <v-app>
    <shiba-navigation-drawer :project="project"/>
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
      return {
        project: {}
      }
    },
    mounted() {
      this.queryProject(this.$route.params.key);
    },
    methods: {
      queryProject(key) {
        this.$axios.get(`/api/project/${key}/`).then(({data}) => {
          this.project = data.result;
        })
      },
    }
  }
</script>
