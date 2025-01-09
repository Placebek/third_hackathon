import { createApp } from 'vue';
import { OhVueIcon, addIcons } from "oh-vue-icons";
import { FaFlag, RiZhihuFill } from "oh-vue-icons/icons";

import App from './App.vue';
import router from './router';
import './index.css';

addIcons(FaFlag, RiZhihuFill);

createApp(App)
  .use(router)
  .component("v-icon", OhVueIcon)
  .mount('#app');
