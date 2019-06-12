<template>
  <v-card :to="`/project/${project.key}`" min-height="150px" max-height="150px">
    <v-card-title primary-title>
      <v-icon left>
        help_outline
      </v-icon>
      <span class="font-weight-medium subheading">{{project.name}}</span>
      <div>
        {{project.owner}}
      </div>
    </v-card-title>
    <v-card-text>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: "ProjectInfoCard",
    props: {
      project: {
        type: Object
      }
    }
  }
</script>

<style scoped>

</style>
