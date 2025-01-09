<template>
  <div>
    <div :class="['bg-gradient-to-l rounded-lg fixed button-0 left-0 w-full z-[99998]', theme === 'dark' ? ' bg-[#1c1c1c] text-white' : ' bg-[#f5f2f2] text-black']">
      <div class="h-[50px]">
        <div class="flex items-end justify-end pr-6 mt-3 gap-3">
          <div @click="toggleTheme" class="cursor-pointer transition-all">
            <v-icon
              v-if="theme === 'dark'"
              name="io-sunny"
              class="cursor-pointer transition-all text-[30px]"
            />
            <v-icon
              v-else
              name="io-moon"
              class="cursor-pointer transition-all text-[30px]"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { addIcons } from "oh-vue-icons";
import { IoSunny, IoMoon } from "oh-vue-icons/icons";

addIcons(IoSunny); 
addIcons(IoMoon); 

export default {
  name: "FootMenu",
  props: {
    theme: {
      type: String,
      required: true,
    },
  },
  methods: {
    toggleTheme() {
      this.$emit("toggle-theme");
    },
  },
};
</script>

<style scoped>
</style>
