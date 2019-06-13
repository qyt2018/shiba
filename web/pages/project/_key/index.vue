<template>
  <v-card height="100%">
    <v-card-title>
      <span class="title font-weight-black">主页</span>
    </v-card-title>
    <v-divider/>
    <v-card-text>
      <v-layout>
        <v-flex xs12>
          <v-container>
            <v-card
              class="text-xs-center"
              color="green"
              dark
            >
              <v-card-text>
                <v-sheet color="rgba(0, 0, 0, .12)">
                  <v-sparkline
                    :value="value"
                    color="rgba(255, 255, 255, .7)"
                    padding="24"
                    stroke-linecap="round"
                    smooth
                  >
                    <template v-slot:label="item">
                      ${{ item.value }}
                    </template>
                  </v-sparkline>
                </v-sheet>
              </v-card-text>

            </v-card>
          </v-container>
        </v-flex>
        <v-flex>

        </v-flex>
        <v-flex>

        </v-flex>
      </v-layout>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    layout: "project",
    head() {
      return {
        title: "项目主页"
      }
    },
    data() {
      return {
        labels: [
          '12am',
          '3am',
          '6am',
          '9am',
          '12pm',
          '3pm',
          '6pm',
          '9pm'
        ],
        value: [
          200,
          675,
          410,
          390,
          310,
          460,
          250,
          240
        ]
      }
    }
  }
</script>
