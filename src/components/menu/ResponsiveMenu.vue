<template>
  <div class="">
    <div :class="['fixed top-0 z-[99999] h-full transition-all bg-[#966acc] text-white duration-500 pt-6 pb-6 px-8 flex flex-col justify-between md:hidden', showMenu ? 'right-0' : '-right-[100%]']">
      <div>
        <div class="flex items-center justify-center gap-3">
          <button 
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
          <v-icon name="hi-solid-user-circle" class="h-[50px]"/>
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
              <!-- <router-link to="/dashboard" class="text-[#8f8f8f] hover:text-white"> -->
                Contact
              <!-- </router-link> -->
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

import { addIcons } from "oh-vue-icons";
import { HiSolidUserCircle } from "oh-vue-icons/icons";

addIcons(HiSolidUserCircle); 

export default {
  components: {
  },
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
  }
};
</script>

<style scoped>
</style>
