<template>
  <div class="login">
    <h1>Welcome to Vumbua</h1>
    <h3>{{ message }}</h3>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      message: "Share your Knowledge"
    };
  }
};
</script>

<style scoped>
h3 {
  color: gray;
}
</style>
