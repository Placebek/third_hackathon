<template>
  <div class="bg-[#0A0A0A] h-full">
    <Navbar />
    <div>
      <div class="flex justify-center items-center py-4 m t-12 p-4">
        <div class="relative w-full max-w-md text-white">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search..."
            class="mt-3 pl-4 w-full p-2 rounded-3xl bg-[#1c1c1c] focus:ring-1 focus:ring-[#7143a8] focus:outline-none"
          />
        </div>
      </div>
    </div>
    <div class="grid grid-cols-2 gap-5 p-3 sm:grid-cols-2 lg:grid-cols-3 text-white">
      <div 
        v-for="(item, index) in results" 
        :key="index" 
        class="h-[330px] w-full bg-[#1c1c1c] rounded-lg overflow-hidden"
        @click="goToMainBook(item.id)"
      >
        <!-- Image Section -->
        <div class="h-[200px] w-full bg-[#966acc]">
          <img v-if="item?.initial_picture" :src="item.initial_picture" alt="fffff" class="" />
          <p v-else>Image not available</p> <!-- Fallback text if no image is available -->
        </div>
        
        <!-- Text Content -->
        <div class="p-2">
          <div class="text-xl font-semibold">{{ item.title }}</div>
          <p class="mt-2 text-sm text-justify">{{ item.subtitle }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { addIcons } from "oh-vue-icons";
import { BiSearch } from "oh-vue-icons/icons";
import Navbar from "../menu/Navbar.vue";
import axios from "axios";
import { useRouter } from 'vue-router'; 

addIcons(BiSearch);

export default {
  name: "Dashboard",
  components: {
    Navbar
  },
  setup() {
    const searchQuery = ref("");  // Модель для поискового запроса
    const router = useRouter();
    const results = ref([]); // Сюда будут сохраняться результаты поиска

    // Функция для выполнения запроса
    const onSearch = async () => {
      try {
        const accessToken = localStorage.getItem("access_token");

        if (!accessToken) {
          throw new Error("Токен доступа не найден. Пожалуйста, выполните вход.");
        }

        const response = await axios.get("http://172.20.10.3:8000/user/stories", {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        results.value = response.data;
        if (results.value.length === 0) {
          alert("Ничего не найдено по запросу.");
        }
      } catch (error) {
        console.error("Ошибка при поиске:", error);
        alert("Ошибка при поиске, попробуйте снова.");
      }
    };

    const goToMainBook = (id) => {
      router.push({ name: 'MainBook', params: { id } });  // Передаем id в параметры маршрута
    };

    onMounted(() => {
      onSearch();
    });

    return {
      searchQuery,
      results,
      onSearch,
      goToMainBook,
    };
  },
};
</script>

<style scoped>
</style>
