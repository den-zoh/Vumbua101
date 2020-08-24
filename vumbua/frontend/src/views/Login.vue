<template>
  <div class="wrapper">
    <div class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-40 md-small-size-66 md-xsmall-size-100 md-medium-size-40 mx-auto"
          >
            <md-card class="md-card-login pa-3">
              <h3 class="form-title">Login</h3>
              <md-card-area class="pa-3">
                <div class="mt-4">
                  <v-text-field
                    v-model="username"
                    label="User Name"
                    :error-messages="nameErrors"
                    @input="$v.username.$touch()"
                  ></v-text-field>
                  <v-text-field
                    v-model="password"
                    label="Password"
                    :type="passwordFieldType"
                    :error-messages="passwordErrors"
                    @input="$v.password.$touch()"
                  >
                    <v-icon
                      v-if="!showPassword"
                      slot="append"
                      @click="togglePasswordVisibility(true)"
                      >visibility</v-icon
                    >
                    <v-icon
                      v-else
                      slot="append"
                      @click="togglePasswordVisibility(false)"
                      >visibility_off</v-icon
                    >
                  </v-text-field>
                </div>
                <div class="row text-center justify-center pb-2">
                  <md-button class="md-primary mr-4 new-font" @click="submit"
                    >login</md-button
                  >
                  <a
                    href="/forgot-password"
                    class="text-primary align-self-center new-font"
                    >Forgot Password?</a
                  >
                </div>
              </md-card-area>

              <md-card-actions md-alignment="left" class="new-font">
                <div>
                  Need an account
                  <a class="text-primary" href="/signup">Sign Up Now</a>
                </div>
              </md-card-actions>
            </md-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";

export default {
  bodyClass: "login-page",
  name: "Login",
  data() {
    return {
      username: null,
      password: null,
      passwordFieldType: "password",
      showPassword: false
    };
  },
  validations: {
    username: { required },
    password: { required }
  },
  props: {
    header: {
      type: String,
      default: require("@/assets/login.jpg")
    }
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.username.$dirty) return errors;
      !this.$v.username.required && errors.push("username is required.");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.required && errors.push("password is required.");
      return errors;
    }
  },
  methods: {
    togglePasswordVisibility(status) {
      this.passwordFieldType =
        this.passwordFieldType === "password" ? "text" : "password";
      this.showPassword = status;
    },
    submit() {
      this.$v.$touch();
      if (!this.$v.$invalid) {
        // eslint-disable-next-line no-unused-vars
        let data = {
          username: this.username,
          password: this.password
        };
      }
    }
  }
};
</script>

<style lang="css">
.form-title {
  text-transform: uppercase;
  font-size: 25px;
  text-align: center;
  margin-bottom: 8px;
}
.md-card {
  border-radius: 0 !important;
}
</style>
