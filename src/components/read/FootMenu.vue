<template>
  <div>
    <div
      :class="[
        'bg-gradient-to-l rounded-lg fixed button-0 left-0 w-full z-[99998]',
        theme === 'dark' ? 'bg-[#1c1c1c] text-white' : 'bg-[#f5f2f2] text-black'
      ]"
    >
      <div class="flex-container">
        <div class="flex-item">
          <div @click="toggleTheme" class="cursor-pointer transition-all">
            <v-icon
              v-if="theme === 'dark'"
              name="io-sunny"
              class="cursor-pointer transition-all w-[25px] h-[25px]"
            />
            <v-icon
              v-else
              name="io-moon"
              class="cursor-pointer transition-all w-[25px] h-[25px]"
            />
          </div>
        </div>

        <div class="flex-item">
          <h1 class="text-xl font-bold">Page {{ currentPage }}</h1>
          <div v-if="loading">Loading...</div>
          <div v-else>
            <p v-for="(line, index) in content" :key="index">{{ line }}</p>
          </div>
        </div>

        <div class="flex-item gap-3">
          <v-icon 
            name="io-arrow-back-circle"
            @click="goToPreviousPage"
            :class="{ 'opacity-50 cursor-not-allowed': currentPage === 1 }"
            :disabled="currentPage === 1"
            class="w-[30px] h-[30px]" 
          />
          <v-icon 
            name="io-arrow-forward-circle"
            @click="goToNextPage"
            :class="{ 'opacity-50 cursor-not-allowed': !hasNextPage }"
            :disabled="!hasNextPage"
            class="w-[30px] h-[30px]"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";
import {
  IoSunny,
  IoMoon,
  IoArrowForwardCircle,
  IoArrowBackCircle,
} from "oh-vue-icons/icons";
import { addIcons } from "oh-vue-icons";

addIcons(IoSunny, IoMoon, IoArrowForwardCircle, IoArrowBackCircle);

export default {
  props: {
    theme: {
      type: String,
      required: true,
    },
  },
  setup() {
    const currentPage = ref(1); // Текущая страница
    const content = ref([]); // Контент страницы
    const hasNextPage = ref(true); // Есть ли следующая страница
    const loading = ref(false);

    const fetchPage = async () => {
      loading.value = true;
      try {
        const response = await axios.get(
          `http://172.20.10.3:8000/book?page=${currentPage.value}`
        );
        content.value = response.data.content;
        hasNextPage.value = response.data.has_next_page;
      } catch (error) {
        console.error("Ошибка при загрузке страницы:", error);
      } finally {
        loading.value = false;
      }
    };

    const goToPreviousPage = () => {
      if (currentPage.value > 1) {
        currentPage.value -= 1;
        fetchPage();
      }
    };

    const goToNextPage = () => {
      if (hasNextPage.value) {
        currentPage.value += 1;
        fetchPage();
      }
    };

    onMounted(() => {
      fetchPage(); // Загружаем первую страницу при монтировании
    });

    return {
      currentPage,
      content,
      hasNextPage,
      loading,
      goToPreviousPage,
      goToNextPage,
    };
  },
  methods: {
    toggleTheme() {
      this.$emit("toggle-theme");
    },
  },
};
</script>


<style scoped>
.flex-container {
  display: flex; /* Горизонтальное расположение элементов */
  flex-direction: row-reverse; /* Обратный порядок */
  justify-content: space-between; /* Пространство между элементами */
  align-items: center; /* Выравнивание по вертикали */
  padding: 10px;
}

.flex-item {
  display: flex; /* Каждый элемент может содержать свои внутренние элементы */
  align-items: center; /* Вертикальное выравнивание */
  gap: 10px; /* Расстояние между вложенными элементами */
}
</style>
