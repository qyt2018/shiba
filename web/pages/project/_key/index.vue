<template>
  <v-card height="100%">
    <v-card-title>
      <span class="title font-weight-black">主页</span>
    </v-card-title>
    <v-divider/>
    <v-card-text>
      <v-container>
        <v-layout wrap>
          <v-flex xs12>
            <v-card
              class="mx-auto mb-4"
              color="grey lighten-4"
              max-width="80%"
            >
              <v-card-title>
                <v-icon
                  :color="checking ? 'red lighten-2' : 'indigo'"
                  class="mr-5"
                  size="64"
                  @click="takePulse"
                >
                  cached
                </v-icon>
                <v-layout
                  column
                  align-start
                >
                  <div class="caption grey--text text-uppercase">
                    Heart rate
                  </div>
                  <div>
          <span
            class="display-2 font-weight-black"
            v-text="avg || '—'"
          ></span>
                    <strong v-if="avg">BPM</strong>
                  </div>
                </v-layout>

                <v-spacer></v-spacer>

                <v-btn icon class="align-self-start" size="28">
                  <v-icon>mdi-arrow-right-thick</v-icon>
                </v-btn>
              </v-card-title>

              <v-sheet color="transparent">
                <v-sparkline
                  :key="String(avg)"
                  :smooth="16"
                  :gradient="['#f72047', '#ffd200', '#1feaea']"
                  :line-width="3"
                  :value="heartbeats"
                  auto-draw
                  stroke-linecap="round"
                ></v-sparkline>
              </v-sheet>
            </v-card>
          </v-flex>
          <v-flex>
            <v-card
              class="ma-3"
            >
              <v-sheet
                class="v-sheet--offset mx-auto"
                color="cyan"
                elevation="12"
                max-width="calc(100% - 32px)"
              >
                <v-sparkline
                  :labels="labels"
                  :value="value"
                  color="white"
                  line-width="2"
                  padding="16"
                ></v-sparkline>
              </v-sheet>

              <v-card-text class="pt-0">
                <div class="title font-weight-light mb-2">User Registrations</div>
                <div class="subheading font-weight-light grey--text">Last Campaign Performance</div>
                <v-divider class="my-2"></v-divider>
                <v-icon
                  class="mr-2"
                  small
                >
                  mdi-clock
                </v-icon>
                <span class="caption grey--text font-weight-light">last registration 26 minutes ago</span>
              </v-card-text>
            </v-card>
          </v-flex>
          <v-flex>
            <v-card
              class="ma-3"
            >
              <v-sheet
                class="v-sheet--offset mx-auto"
                color="cyan"
                elevation="12"
                max-width="calc(100% - 32px)"
              >
                <v-sparkline
                  :labels="labels"
                  :value="value"
                  color="white"
                  line-width="2"
                  padding="16"
                ></v-sparkline>
              </v-sheet>

              <v-card-text class="pt-0">
                <div class="title font-weight-light mb-2">User Registrations</div>
                <div class="subheading font-weight-light grey--text">Last Campaign Performance</div>
                <v-divider class="my-2"></v-divider>
                <v-icon
                  class="mr-2"
                  small
                >
                  mdi-clock
                </v-icon>
                <span class="caption grey--text font-weight-light">last registration 26 minutes ago</span>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
  const exhale = ms =>
    new Promise(resolve => setTimeout(resolve, ms));
  export default {
    layout: "project",
    head() {
      return {
        title: "项目主页"
      }
    },
    data() {
      return {
        checking: false,
        heartbeats: [],
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
    },
    computed: {
      avg() {
        const sum = this.heartbeats.reduce((acc, cur) => acc + cur, 0)
        const length = this.heartbeats.length

        if (!sum && !length) return 0

        return Math.ceil(sum / length)
      }
    },

    created() {
      this.takePulse(false)
    },

    methods: {
      heartbeat() {
        return Math.ceil(Math.random() * (120 - 80) + 80)
      },
      async takePulse(inhale = true) {
        this.checking = true

        inhale && await exhale(1000)

        this.heartbeats = Array.from({length: 20}, this.heartbeat)

        this.checking = false
      }
    }
  }
</script>
