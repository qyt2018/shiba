<template>
  <v-card :to="`/project/${project.key}`" height="230px">
    <v-card-title primary-title>
      <v-icon left>
        help_outline
      </v-icon>
      <span class="font-weight-medium subheading">{{project.name}}</span>
    </v-card-title>
    <v-card-text>
      {{project.key}}
    </v-card-text>
    <v-card-actions>
      <v-list-tile v-if="project.owner" class="grow">
        <v-list-tile-avatar color="grey darken-3">
          <v-img
            class="elevation-6"
            src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
          ></v-img>
        </v-list-tile-avatar>

        <v-list-tile-content>
          <v-list-tile-title>{{project.owner.name}}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-card-actions>
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
