<template>
  <v-card height="230px">
    <project-edit-dialog @close="closeEditProjectDialog" :projectId="currentProjectId" :visible="editDialogVisible"/>
    <v-card-title primary-title>
      <nuxt-link style="text-decoration: none; color: #000;" class="ml-2" :to="`/project/${project.key}`">
        <span class="font-weight-medium subheading">{{project.name}}</span>
      </nuxt-link>
      <v-spacer/>
      <v-menu bottom left>
        <template v-slot:activator="{ on }">
          <v-btn
            icon
            v-on="on"
          >
            <v-icon>list</v-icon>
          </v-btn>
        </template>
        <v-list dense>
          <v-list-tile
            @click="editProject(project.id)"
          >
            <v-list-tile-action>
              <v-icon>edit</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>编辑</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile
            @click="deleteProject(project.id)"
            color="error"
          >
            <v-list-tile-action>
              <v-icon color="error">delete</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>删除</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-card-title>
    <v-card-text>
      <v-layout class="ml-2">
        <v-flex class="ml-2">
          <v-badge
            left
            overlap
            color="pink"
          >
            <template v-slot:badge>
              <span>6</span>
            </template>
            <v-btn :to="`/project/${project.key}/app`" small outline>
              未开始
            </v-btn>
          </v-badge>
        </v-flex>
        <v-flex class="ml-2">
          <v-badge
            left
            overlap
            color="indigo"
          >
            <template v-slot:badge>
              <span>6</span>
            </template>
            <v-btn :to="`/project/${project.key}/task`" small outline>
              进行中
            </v-btn>
          </v-badge>
        </v-flex>
        <v-flex class="ml-2">
          <v-badge
            left
            overlap
            color="purple"
          >
            <template v-slot:badge>
              <span>6</span>
            </template>
            <v-btn :to="`/project/${project.key}/user`" small outline>
              堵塞
            </v-btn>
          </v-badge>
        </v-flex>
      </v-layout>
    </v-card-text>
    <v-card-actions>
      <v-list-tile v-if="project.owner" class="grow">
        <v-list-tile-avatar>
          <v-icon>
            account_circle
          </v-icon>
        </v-list-tile-avatar>

        <v-list-tile-content>
          <v-list-tile-title>{{project.owner.name}}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-card-actions>
  </v-card>
</template>

<script>
  import ProjectEditDialog from '@/components/project/edit-dialog'

  export default {
    components: {
      ProjectEditDialog
    },
    name: "ProjectInfoCard",
    data() {
      return {
        currentProjectId: null,
        editDialogVisible: false
      }
    },
    props: {
      project: {
        type: Object
      }
    },
    methods: {
      closeEditProjectDialog() {
        this.currentProjectId = null;
        this.editDialogVisible = false;
        this.$emit('success');
      },
      editProject(id) {
        this.currentProjectId = id;
        this.editDialogVisible = true;
      },
      deleteProject(id) {
        this.$confirm('确定删除吗？').then(res => {
          if (res) {
            this.$axios.post(`/api/project/${id}/delete`).then(({data}) => {
              this.$toast.success("删除成功");
              this.$emit('success');
            })
          }
        })
      }
    }
  }
</script>

<style scoped>
</style>
