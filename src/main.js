import { createApp } from 'vue';
import { OhVueIcon, addIcons } from "oh-vue-icons";
import { FaFlag, RiZhihuFill } from "oh-vue-icons/icons";

import App from './App.vue';
import router from './router';
import './index.css';
import { createPinia } from 'pinia';

const pinia = createPinia();
addIcons(FaFlag, RiZhihuFill);

createApp(App)
  .use(router)
  .use(pinia) 
  .component("v-icon", OhVueIcon)
  .mount('#app');
