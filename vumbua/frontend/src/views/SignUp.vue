<template>
  <div class="wrapper">
    <div class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-66 md-small-size-66 md-xsmall-size-100 md-medium-size-66 mx-auto"
          >
            <md-card class="md-card-login pa-3">
              <h3 class="form-title">Registration</h3>
              <md-card-area class="pa-3">
                <div class="row">
                  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <v-text-field
                      label="User Name *"
                      dense
                      v-model="username"
                      :error-messages="nameErrors"
                      @input="$v.username.$touch()"
                      @blur="$v.username.$touch()"
                    ></v-text-field>
                  </div>
                  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <v-text-field
                      label="Email *"
                      dense
                      type="email"
                      v-model="email"
                      :error-messages="emailErrors"
                      @input="$v.email.$touch()"
                      @blur="$v.email.$touch()"
                    ></v-text-field>
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <v-select
                      :items="genders"
                      dense
                      label="Gender *"
                      v-model="gender"
                      :error-messages="genderErrors"
                      @input="$v.gender.$touch()"
                      @blur="$v.gender.$touch()"
                    ></v-select>
                  </div>
                  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <v-select
                      :items="categories"
                      item-text="state"
                      item-value="abbr"
                      label="Category *"
                      dense
                      return-object
                      v-model="category"
                      :error-messages="categoryErrors"
                      @input="$v.category.$touch()"
                      @blur="$v.category.$touch()"
                    ></v-select>
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <v-text-field
                      label="Phone Number *"
                      dense
                      type="text"
                      v-model="phone_number"
                      :error-messages="phoneErrors"
                      @input="$v.phone_number.$touch()"
                      @blur="$v.phone_number.$touch()"
                    ></v-text-field>
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <v-text-field
                      label="Password *"
                      dense
                      :type="passwordFieldType"
                      v-model="password"
                      :error-messages="passwordErrors"
                      @input="$v.password.$touch()"
                      @blur="$v.password.$touch()"
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
                  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                    <v-text-field
                      label="Password Confirmation *"
                      dense
                      type="password"
                      v-model="confirm_password"
                      :error-messages="confirmErrors"
                      @input="$v.confirm_password.$touch()"
                      @blur="$v.confirm_password.$touch()"
                    >
                    </v-text-field>
                  </div>
                </div>
                <div class="row text-center justify-center pb-2">
                  <md-button @click="submit" class="md-primary"
                    >sign up</md-button
                  >
                </div>
              </md-card-area>

              <md-card-actions md-alignment="left">
                <div>
                  Already have an Account
                  <a class="text-primary" href="/login">login Now</a>
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
import {
  required,
  minLength,
  maxLength,
  sameAs,
  email
} from "vuelidate/lib/validators";

export default {
  bodyClass: "login-page",
  name: "SignUp",
  data() {
    return {
      username: null,
      email: null,
      gender: null,
      category: null,
      phone_number: null,
      password: null,
      confirm_password: null,
      genders: ["Male", "Female"],
      categories: [
       { state: "IT", abbr: "IT" },
        { state: "Human Resource", abbr: "HR" },
        { state: "Finance", abbr: "FE" },
        { state: "Health", abbr: "HE" },
        { state: "Business", abbr: "BS" },
        { state: "Agriculture", abbr: "AG" },
        { state: "Entertainment", abbr: "ET" }
      ],
      passwordFieldType: "password",
      showPassword: false
    };
  },
  validations: {
    username: { required, maxLength: maxLength(150) },
    email: { required, email },
    gender: { required },
    category: { required },
    phone_number: { required },
    password: { required, minLength: minLength(6) },
    confirm_password: { sameAsPassword: sameAs("password") }
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
      !this.$v.username.maxLength && errors.push("150 Characters or fewer");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.required && errors.push("email is required.");
      !this.$v.email.email && errors.push("field must be an email.");
      return errors;
    },
    genderErrors() {
      const errors = [];
      if (!this.$v.gender.$dirty) return errors;
      !this.$v.gender.required && errors.push("gender is required.");
      return errors;
    },
    categoryErrors() {
      const errors = [];
      if (!this.$v.category.$dirty) return errors;
      !this.$v.category.required && errors.push("category is required.");
      return errors;
    },
    phoneErrors() {
      const errors = [];
      if (!this.$v.phone_number.$dirty) return errors;
      !this.$v.phone_number.required &&
        errors.push("phone number is required.");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.required && errors.push("password is required.");
      !this.$v.password.minLength &&
        errors.push("password must be more than 6 character");
      return errors;
    },
    confirmErrors() {
      const errors = [];
      if (!this.$v.confirm_password.$dirty) return errors;
      !this.$v.confirm_password.sameAsPassword &&
        errors.push("passwords must match");
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
          email: this.email,
          gender: this.gender,
          category: this.category,
          phone: this.phone_number,
          password: this.password
        };
      }
    }
  }
};
</script>

<style lang="css" scoped>
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
