<template>
  <div class="bg-[#0A0A0A] h-full">
    <Navbar />
    <div>
      <div class="flex justify-center items-center py-4 mt-12 p-4">
        <div class="relative w-full max-w-md text-white">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search..."
            class="mt-3 pl-4 w-full p-2 rounded-3xl bg-[#1c1c1c] focus:ring-1 focus:ring-[#7143a8] focus:outline-none"
          />
          <button
            @click="onSearch"
            class="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-500 hover:text-violet-600"
          >
            <v-icon name="bi-search" class="text-lg" />
          </button>
        </div>
      </div>
    </div>
    <div class="grid grid-cols-2 gap-5 p-3 sm:grid-cols-2 lg:grid-cols-3 text-white">
      <div v-for="item in 8" :key="item" class="h-[330px] w-full bg-[#1c1c1c]">
        <div class="h-[200px] w-full bg-[#966acc]">
        </div>
        <div class="p-2 text-justify">
          <div class="text-xl">APT</div>
          <p class="text-sm">Lorem ipsum dolor sit amet consectetur adipisicing elit, dedsd ipsum dolor sit ...</p>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from "vue";
import { addIcons } from "oh-vue-icons";
import { BiSearch } from "oh-vue-icons/icons";
import Navbar from "../menu/Navbar.vue";

addIcons(BiSearch);

export default {
  name: "Dashboard",
  components: {
    Navbar
  },
  setup() {
    const searchQuery = ref("");

    const onSearch = () => {
      // Логика для обработки поиска
      alert(`Поиск по запросу: ${searchQuery.value}`);
    };

    return {
      searchQuery,
      onSearch,
    };
  },
};
</script>

<style scoped>
</style>
