<template>
  <v-card height="100%">
    <v-card-title style="height: 12%">
      <span class="headline font-weight-black">项目列表</span>
      <v-spacer/>
      <v-btn color="primary">创建项目</v-btn>
    </v-card-title>
    <v-divider/>
    <v-layout style="height: 87%">
      <v-flex xs2>
        <v-list dense>
          <template>
            <v-subheader>筛选</v-subheader>
            <v-divider/>
            <v-list-tile avatar @click="">
              <v-list-tile-avatar>
                <v-icon color="primary">assignment</v-icon>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title>所有项目</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile avatar @click="">
              <v-list-tile-avatar>
                <v-icon color="yellow darken-2">assignment_ind</v-icon>
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title>我的项目</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </template>
        </v-list>
      </v-flex>
      <v-divider :vertical="true"/>
      <v-flex xs10>
        <v-container fill-height>
          <v-layout column fill-height>
            <v-flex>
              <v-layout wrap>
                <v-flex v-for="x in 12" :key="x" class="pa-1" xs3>
                  <v-card to="/project/ceshi" min-height="150px" max-height="150px">
                    <v-card-title primary-title>
                      <v-icon left>
                        help_outline
                      </v-icon>
                      <span class="font-weight-medium subheading">项目名称</span>
                    </v-card-title>
                    <v-card-text>
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex align-self-center class="pt-2">
              <v-pagination :value="1" :length="6"></v-pagination>
            </v-flex>
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
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
