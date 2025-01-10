<template>
  <div class="bg-[#0A0A0A] h-full">
    <Navbar />
    <div>
      <div class="mt-12 text-white">
        <div class="flex justify-center items-end relative w-full h-[400px] bottom-0 bg-gradient-to-t from-black">
          <img v-if="selectedItem?.initial_picture" :src="getFullImagePath(selectedItem.initial_picture)" alt="Image not available"
          class="blur-[5px] w-full h-full absolute top-0 left-0">

          <img v-if="selectedItem?.initial_picture" :src="getFullImagePath(selectedItem.initial_picture)" alt="Image not available" class="w-[300px] h-[290px] rounded-xl absolute" />
        </div>
        <div v-if="selectedItem" class="flex items-center flex-col text-center gap-3 p-6">
          <div class="text-3xl">
            <!-- Выводим название книги -->
            {{ selectedItem.title }}
          </div>
          <div class="text-sm">
            <!-- Выводим подзаголовок книги -->
            {{ selectedItem.subtitle }}
          </div>
        </div>
        <div class="px-5">
          <button
            to="/mainbook"
            @click="goToReadBook"
            class="btn-login-f"
          >
            <v-icon name="io-book-sharp" class="" />
            Read
          </button>
        </div>
        <div class="mt-7 w-full h-[500px] bg-[#1c1c1c] rounded-lg">
          <div class="flex items-center justify-center flex-row gap-16 p-3 border-b-[1px] border-gray-500">
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
          <div v-if="selected === 'about'">
            <About :story-id="route.params.id" />
          </div>
          <div v-if="selected === 'charpets'">
            <Charpets :story-id="route.params.id" />
          </div>
          <div v-if="selected === 'status'">
            <Status :story-id="route.params.id" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { addIcons } from "oh-vue-icons";
import { IoBookSharp } from "oh-vue-icons/icons";
import Navbar from "../menu/Navbar.vue";
import { useRouter, useRoute } from 'vue-router';
import About from './About.vue';
import Charpets from './Charpets.vue';
import Status from './Status.vue';
import axios from 'axios';

addIcons(IoBookSharp);

export default {
  name: "MainBook",
  props: {
    storyId: {
      type: String,
      required: true,
    },
  },
  components: {
    Navbar,
    About,
    Status,
    Charpets
  },
  data() {
    return {
      selected: 'about' // По умолчанию показываем вкладку 'about'
    };
  },
  methods: {
    selectTab(tab) {
      this.selected = tab; // При клике меняем выбранную вкладку
    }
  },
  setup() {
    const route = useRoute(); // Получаем текущие параметры маршрута
    const router = useRouter(); // Получаем доступ к роутеру
    const selectedItem = ref(null); // Для хранения данных, полученных с API

    const storyId = route.params.id;
    console.log("ID: ", storyId);

    const goToReadBook = () => {
      router.push('/readbook');
    };

    // Функция для формирования полного пути к изображению
    const getFullImagePath = (relativePath) => {
      return `http://172.20.10.3:8000${relativePath}`; // Добавляем базовый URL
    };

    onMounted(() => {
      axios.get(`http://172.20.10.3:8000/user/stories/${storyId}`)
        .then(response => {
          selectedItem.value = response.data;
        })
        .catch(error => {
          console.error('Error fetching item data:', error);
        });
    });
    
    return {
      route,
      goToReadBook,
      selectedItem,
      getFullImagePath,
    };
  }
};
</script>

<style scoped>
</style>
