<template>
  <v-card height="100%">
    <project-create-dialog :visible.sync="createDialogVisible" @close="closeDialog"/>
    <v-card-title style="height: 12%">
      <span class="headline font-weight-black">项目列表</span>
      <v-spacer/>
      <v-btn color="primary" @click="createDialogVisible = true">创建项目</v-btn>
    </v-card-title>
    <v-divider/>
    <v-layout style="height: 79%">
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
        <div class="ml-5 mt-3" style="max-width: 20%">
          <v-text-field prepend-icon="search" v-model="search" label="搜索......"></v-text-field>
        </div>
        <v-container fill-height>
          <v-layout column fill-height>
            <v-flex>
              <v-layout wrap>
                <v-flex v-for="project in result" :key="project.id" class="pa-1" xs3>
                  <project-info-card :project="project"/>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex class="pt-2">
              <div class="text-xs-center">
                <v-pagination v-model="currentPage" :total-visible="6" :length="pageCount"></v-pagination>
              </div>
            </v-flex>
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
  import ProjectCreateDialog from '@/components/project/create-dialog'
  import ProjectInfoCard from '@/components/project/info-card'

  export default {
    components: {
      ProjectCreateDialog,
      ProjectInfoCard
    },
    head() {
      return {
        title: "项目"
      }
    },
    data() {
      return {
        result: [],
        createDialogVisible: false,
        currentPage: 1,
        pageCount: 0,
        search: ""
      }
    },
    watch: {
      currentPage() {
        this.queryList();
      },
      search: _.debounce(function () {
        this.currentPage = 1;
        this.queryList()
      }, 300)
    },
    mounted() {
      this.queryList();
    },
    methods: {
      queryList() {
        this.$axios.get("/api/project/", {
          params: {
            page: this.currentPage,
            per_page: 8,
            search: this.search
          }
        }).then(({data}) => {
          this.result = data.result.objects;
          this.pageCount = data.result.page_count;
        })
      },
      closeDialog() {
        this.createDialogVisible = false;
        this.queryList();
      }
    }
  }
</script>
