<template>
  <footer class="footer" style="background-color: #1c2431; position: static">
    <div class="container">
      <div class="md-layout">
        <div
          class="md-layout-item md-size-35 md-xsmall-size-100 md-small-size-50 md-medium-size-35 text-white"
        >
          <div class="title uppercase text-white">
            <h3>vumbua</h3>
          </div>
          <h4>
            Vumbua offers a number of incubation programmes in the
            Bioeconomy(agro processing and pharmaceutical), Smart Industries(ICT
            and advanced manufacturing) and Green Economy (Water purification,
            waste management and renewable energy).
          </h4>
        </div>
        <div
          class="md-layout-item md-size-20 md-xsmall-size-100 md-small-size-50 md-medium-size-20"
        >
          <div class="title uppercase text-white">
            <h3>services</h3>
          </div>
          <div class="text-white">
            <h4>Incubation</h4>
            <h4>Idea Development</h4>
            <h4>Mentorship</h4>
          </div>
        </div>
        <div
          class="md-layout-item md-size-20 md-xsmall-size-100 md-small-size-50 md-medium-size-20"
        >
          <div class="title uppercase text-white">
            <h3>links</h3>
          </div>
          <div class="text-white">
            <h4>Home</h4>
            <h4>About Us</h4>
            <h4>Contact Us</h4>
            <h4>Help</h4>
          </div>
        </div>
        <div
          class="md-layout-item md-size-25 md-xsmall-size-100 md-small-size-50 md-medium-size-25"
        >
          <div class="title uppercase text-white">
            <h3>contact</h3>
          </div>
          <div class="text-white md-white">
            <h4>
              <md-icon class="text-white ma-3">home</md-icon>Ole Sangale Road,
              Madaraka, Nairobi
            </h4>
            <h4>
              <md-icon class="text-white ma-3">email</md-icon>info@vumbua.org
            </h4>
            <h4>
              <md-icon class="text-white ma-3">phone</md-icon>+ 254 738585470
            </h4>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="md-layout">
        <div class="md-layout-item text-white text-center">
          <div class="copyright">
            &copy; {{ year }} Copyright:
            <a href="#" class="text-white">www.SADACrenewed.com</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      year: new Date().getFullYear()
    };
  }
};
</script>
<style>
.uppercase {
  text-transform: uppercase !important;
}
.text-white {
  color: white !important;
}
.ma-3 {
  padding-right: 20px;
}
.footer .container .md-layout {
  font-family: "Times New Roman", serif;
}
</style>
