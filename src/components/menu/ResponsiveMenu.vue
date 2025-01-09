<template>
  <div :class="theme">
    <div :class="['fixed top-0 z-[99999] h-full transition-all bg-[#966acc] text-white duration-500 pt-6 pb-6 px-8 flex flex-col justify-between md:hidden', showMenu ? 'right-0' : '-right-[100%]']">
      <div>
        <div class="flex items-center justify-center gap-3">
          <button 
            @click="toggleTheme"
            class="btn-menu-f"
          >
            Theme
          </button>
          <button 
            to="/search" 
            class="btn-menu-f"
            @click="goToSerachForm"
          >
            Search
          </button>
        </div>
        <div class="mt-7 flex items-center justify-start gap-3">
          <v-icon name="hi-solid-user-circle" class="h-[50px]" />
          <div>
            <h1 class="text-xl font-semibold">username</h1>
            <h1 class="text-s">username@example.com</h1>
          </div>
        </div>

        <nav class="mt-12 text-white">
          <ul class="space-y-6 text-lg">
            <li>
              <router-link to="/dashboard" class="">
                Home
              </router-link>
            </li>
            <li>
              Contact
            </li>
            <li>
              <router-link to="/settings" class="">
                Settings
              </router-link>
            </li>
          </ul>
        </nav>
      </div>
      <div class="text-sm">
        <p>@2024 All Rights Reserved</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from "vue";
import { addIcons } from "oh-vue-icons";
import { HiSolidUserCircle } from "oh-vue-icons/icons";

addIcons(HiSolidUserCircle);

export default {
  props: {
    showMenu: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    goToSerachForm() {
      this.$router.push('/serach');
    },
  },
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

    return {
      theme,
      toggleTheme
    };
  }
};
</script>

<style scoped>
</style>