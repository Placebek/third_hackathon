<template>
  <div class="bg-[#0A0A0A] h-full">
    <Navbar />
    <div>
      <div class="mt-12 text-white ">
        <div class="flex justify-center items-end relative w-full h-[400px] bottom-0 bg-gradient-to-t from-black">
          <div class="blur-[5px] w-full h-full absolute top-0 left-0 login-bg-img">
          </div>
          
          <div class="w-[250px] h-[320px] rounded-xl login-bg-img absolute ">
          </div>
        </div>
        <div class="flex items-center flex-col text-center gap-3 p-6">
          <div class="text-3xl">
            PUSS IN BOOTS
          </div>
          <div class="text-sm">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea neque nisi deserunt, quos accusantium ullam 
          </div>
        </div>
        <div class="px-5">
          <button class="btn-login-f">
            <v-icon name="io-book-sharp" class=""/>
            Read
          </button>
        </div>
        <div class="mt-7 w-full h-[500px] bg-[#1c1c1c] rounded-lg">
          <div class="flex items-center justify-center flex-row gap-16 p-3">
            <div
              :class="{'text-white': selected === 'about', 'text-[#8f8f8f]': selected !== 'about'}"
              @click="selectTab('about')"
            >
              about
            </div>
            <div
              :class="{'text-white': selected === 'charpets', 'text-[#8f8f8f]': selected !== 'charpets'}"
              @click="selectTab('charpets')"
            >
              charpets
            </div>
            <div
              :class="{'text-white': selected === 'status', 'text-[#8f8f8f]': selected !== 'status'}"
              @click="selectTab('status')"
            >
              status
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { addIcons } from "oh-vue-icons";
import { IoBookSharp } from "oh-vue-icons/icons";
import Navbar from "../menu/Navbar.vue";

addIcons(IoBookSharp);

export default {
  name: "MainBook",
  components: {
    Navbar,
    
  },
  data() {
    return {
      selected: 'about'
    };
  },
  methods: {
    selectTab(tab) {
      this.selected = tab;
    }
  }
};
</script>

<style scoped>
</style>
