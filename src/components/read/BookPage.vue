<template>
    <div :class="['w-full h-screen', theme === 'dark' ? 'bg-[#0A0A0A]' : 'bg-white']">
      <Navbar />
      <div>
        <div :class="['flex items-center justify-center mt-10 p-2', theme === 'dark' ? 'text-white' : 'text-black']">
          <div class="flex items-center flex-col text-center gap-2 p-2">
            <div class="text-justify mt-5 text-lg indent-8">
              <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci nemo velit eveniet quia sequi, reiciendis magni, provident laborum quod officia nobis. Odit vel libero minima, ipsa ducimus aut quibusdam veritatis.
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero nostrum, dignissimos perferendis porro, a quisquam ipsam expedita quasi dolorum adipisci provident. Illo quidem nesciunt, beatae vel quae quas? Assumenda, eum!</p>
              <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero nostrum, dignissimos perferendis porro, a quisquam ipsam expedita quasi dolorum adipisci provident. Illo quidem nesciunt, beatae vel quae quas? Assumenda, eum!</p>
            </div>
          </div>
        </div>
      </div>
      <FootMenu :theme="theme" @toggle-theme="toggleTheme" />
    </div>
  </template>
  
  <script>
  import { ref, watch } from "vue";
  import Navbar from "../menu/Navbar.vue";
  import FootMenu from "../read/FootMenu.vue";
  
  export default {
    name: "ReadBook",
    components: {
      Navbar,
      FootMenu,
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
        toggleTheme,
      };
    },
  };
  </script>
  