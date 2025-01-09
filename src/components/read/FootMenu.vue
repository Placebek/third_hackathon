<template>
  <div>
    <div class="bg-gradient-to-l bg-[#1c1c1c] text-white fixed button-0 left-0 w-full z-[99998]">
      <div class="h-[50px]">
        <div class="flex items-center gap-4 text-white">
          <div @click="toggleTheme" class="cursor-pointer transition-all">
            <v-icon
              :is="theme === 'dark' ? 'wi-day-sunny' : 'io-moon'" 
              class="cursor-pointer transition-all text-[30px]"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from "vue";
import { WiDaySunny, IoMoon } from "oh-vue-icons/icons";
import { addIcons } from "oh-vue-icons";

addIcons(WiDaySunny, IoMoon);

export default {
  name: "FootMenu",
  setup() {
    const theme = ref(localStorage.getItem("theme") || "light");

    const toggleTheme = () => {
      theme.value = theme.value === "dark" ? "light" : "dark";
    };

    watch(
      theme,
      (newTheme) => {
        const rootElement = document.documentElement;

        if (newTheme === "dark") {
          rootElement.classList.add("dark");
          localStorage.setItem("theme", "dark");
        } else {
          rootElement.classList.remove("dark");
          localStorage.setItem("theme", "light");
        }
      },
      { immediate: true }
    );

    const showMenu = ref(false);

    const toggleMenu = () => {
      showMenu.value = !showMenu.value;
    };

    return {
      theme,
      toggleTheme,
      showMenu,
      toggleMenu,
    };
  },
};
</script>

<style scoped>
/* Добавьте стили, если необходимо */
</style>
