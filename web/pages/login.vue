<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex sm4>
            <v-card class="elevation-1 pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <img src="~/assets/images/devops_log.png" class="logo_img">
                  <h1 class="flex my-4 primary--text">ShiBa-持续交付</h1>
                </div>
                <v-form ref="login_form" @keyup.native.enter="login" lazy-validation>
                  <v-text-field
                    append-icon="person"
                    name="login"
                    label="账号"
                    :rules="rules.username"
                    type="text"
                    required
                    v-model="username"
                  ></v-text-field>
                  <v-text-field
                    append-icon="lock"
                    name="password"
                    label="密码"
                    type="password"
                    required
                    v-model="password"
                    :rules="rules.password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="login" :loading="loading">登陆</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    head() {
      return {
        title: "登陆"
      };
    },
    layout: "blank",
    data: () => ({
      loading: false,
      username: "",
      password: "",
      rules: {
        username: [v => !!v || "不能为空！"],
        password: [v => !!v || "不能为空！"]
      }
    }),
    methods: {
      login() {
        if (this.$refs.login_form.validate()) {
          this.loading = true;
          this.$auth
            .loginWith("local", {
              data: {
                username: this.username,
                password: this.password
              }
            })
            .then(() => {
              this.$router.push("/");
              this.loading = false;
            })
            .catch(() => {
              this.loading = false;
            });
        }
      }
    }
  };
</script>
<style scoped lang="css">
  #login {
    height: 50%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    content: "";
    z-index: 0;
  }

  .logo_img {
    width: auto;
    height: 180px;
    max-width: 100%;
  }
</style>
