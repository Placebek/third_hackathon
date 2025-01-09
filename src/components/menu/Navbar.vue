<template>
  <div class="">
    <nav class="bg-gradient-to-l from-[#7143a8] via-[#7847b3] to-[#966acc] text-white fixed top-0 left-0 w-full z-[99998]">
      <div class="container">
        <div class="flex justify-start py-3 p-3">
          <div @click="toggleMenu" class="cursor-pointer transition-all ">
            <div class="">
              <span v-if="!showMenu">
                <v-icon name="ri-menu-2-fill" class="cursor-pointer transition-all text-[30px]"/>
              </span>
              <span v-else>
                <v-icon name="ri-menu-3-fill" class="cursor-pointer transition-all text-[30px]"/>
              </span>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Responsive Menu -->
    <ResponsiveMenu :showMenu="showMenu" />
  </div>
</template>

<script>

import { ref } from "vue";
import { addIcons } from "oh-vue-icons";
import ResponsiveMenu from './ResponsiveMenu.vue';
import { RiMenu3Fill, RiMenu2Fill } from "oh-vue-icons/icons";
import { IoSunny, IoMoon } from "oh-vue-icons/icons";

addIcons(RiMenu2Fill);
addIcons(RiMenu3Fill);
addIcons(IoSunny); 
addIcons(IoMoon); 

export default {
  name: "NavbarMenu",
  components: {
    ResponsiveMenu,
  },
  setup() {
    const showMenu = ref(false);

    const toggleMenu = () => {
      showMenu.value = !showMenu.value;
    };

    return {
      showMenu,
      toggleMenu
    };
  }
};
</script>

<style scoped>
</style>
