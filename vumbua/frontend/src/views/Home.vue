<template>
  <div class="wrapper">
    <div class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="blob">
          <svg
            xmlns:xlink="http://www.w3.org/1999/xlink"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 310 350"
          >
            <path
              d="M156.4,339.5c31.8-2.5,59.4-26.8,80.2-48.5c28.3-29.5,40.5-47,56.1-85.1c14-34.3,20.7-75.6,2.3-111
          c-18.1-34.8-55.7-58-90.4-72.3c-11.7-4.8-24.1-8.8-36.8-11.5l-0.9-0.9l-0.6,0.6c-27.7-5.8-56.6-6-82.4,3c-38.8,13.6-64,
          48.8-66.8,90.3c-3,43.9,17.8,88.3,33.7,128.8c5.3,13.5,10.4,27.1,14.9,40.9C77.5,309.9,111,343,156.4,339.5z"
            />
          </svg>
        </div>
        <div class="text-center justify-center buttons">
          <h1>welcome to Vumbua!</h1>
          <div class="mt-15">
            <md-button
              href="/signup"
              class="md-white md-round md-lg mr-4"
              style="color: #0d47a1 !important;"
              >sign up</md-button
            >
            <md-button
              href="/login"
              class="md-white md-round md-lg"
              style="color: #0d47a1 !important;"
              >login</md-button
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  props: {
    header: {
      type: String,
      default: require("@/assets/home2.jpg")
    }
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway&display=swap");

h1 {
  color: white;
  font-size: 15vmin;
  line-height: 1;
  font-weight: bold;
  letter-spacing: 2px;
  text-transform: capitalize;
  padding-left: 40px;
  z-index: 5;
  font-family: "Raleway", sans-serif;
}
.buttons {
  z-index: 5;
}

.blob {
  position: absolute;
  top: 0;
  left: 0;
  color: #023f92;
  width: 25vmax;
  z-index: 2;
  animation: move 10s ease-in-out infinite;
  transform-origin: 50% 50%;
}

@keyframes move {
  0% {
    transform: scale(1) translate(10px, -30px);
  }
  38% {
    transform: scale(0.8, 1) translate(80vw, 20vh) rotate(160deg);
  }
  40% {
    transform: scale(0.8, 1) translate(80vw, 20vh) rotate(160deg);
  }
  78% {
    transform: scale(1) translate(0vw, 10vh) rotate(-20deg);
  }
  80% {
    transform: scale(1) translate(0vw, 10vh) rotate(-20deg);
  }
  100% {
    transform: scale(1) translate(10px, -30px);
  }
}
</style>
