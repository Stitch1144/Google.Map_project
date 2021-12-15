import { createApp } from "vue";
import App from "./App.vue";
import VueGoogleMaps from "@fawmi/vue-google-maps";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle";

import { API_KEY } from "./constance";

const app = createApp(App);

app
  .use(VueGoogleMaps, {
    load: {
      key: API_KEY,
      libraries: ["places", "geometry"],
    },
  })
  .mount("#app");
