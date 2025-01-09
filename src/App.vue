<template>
  <div class="bg-[#0A0A0A] h-full">
    <router-view></router-view>
  </div>
</template>

<script>
import { useThemeStore } from '../src/stores/pinia/themeStore';

export default {
  name: "App",
  setup() {
    const themeStore = useThemeStore();

    themeStore.initializeTheme();

    return {
      theme: themeStore.theme,
      toggleTheme: themeStore.toggleTheme,
    };
  },
};

</script>


