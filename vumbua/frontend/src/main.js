import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import MaterialKit from "./plugins/material-kit";
import vuetify from "./plugins/vuetify";
import Vuelidate from "vuelidate";
import Vuetify from "vuetify";
import "material-design-icons-iconfont/dist/material-design-icons.css";

Vue.config.productionTip = false;

Vue.use(MaterialKit);
Vue.use(Vuelidate);
Vue.use(Vuetify);


const NavbarStore = {
  showNavbar: false
};

Vue.mixin({
  data() {
    return {
      NavbarStore
    };
  }
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
