<template>
  <v-card>
    <v-btn @click="$toast.custom('Info toast')">custom</v-btn>
    <v-btn @click="$toast.info('Info toast')">info</v-btn>
    <v-btn @click="$toast.success('Info toast')">success</v-btn>
    <v-btn @click="$toast.error('Info toast')">error</v-btn>
    <v-btn @click="$toast.warning('Info toast')">warning</v-btn>
    <div>asdjflkasdj</div>
  </v-card>
</template>

<script>
  export default {
    data() {
      return {
        result: null
      }
    },
    mounted() {
      this.$axios.get("/api/project/").then(({data}) => {
        this.result = data;
      })
    }
  }
</script>
