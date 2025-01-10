<template>
  <div>
    <div :class="['fixed top-0 z-[99999] h-full w-[250px] transition-all bg-[#966acc] text-white duration-500 pt-6 pb-6 px-8 flex flex-col justify-between md:hidden', showMenu ? 'right-0' : '-right-[100%]']">
      <div>
        <!-- Кнопка поиска -->
        <div class="flex items-center justify-center gap-3">
          <button 
            to="/search" 
            class="btn-menu-f"
            @click="goToSearch"
          >
            Search
          </button>
        </div>
        <!-- Профиль пользователя -->
        <div class="mt-7 flex items-center justify-start gap-3">
          <div class="mt-2">
            <v-icon name="hi-solid-user-circle" class="h-[48px] w-[48px]" />
          </div>
          <div>
            <h1 class="text-xl font-semibold">{{ userData?.username || 'Guest' }}</h1>
            <h1 class="text-s">{{ userData?.email || 'No email available' }}</h1>
          </div>
        </div>
        <!-- Меню навигации -->
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
      <!-- Подвал -->
      <div class="text-sm">
        <p>@2025 All Rights Reserved</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { addIcons } from "oh-vue-icons";
import { HiSolidUserCircle } from "oh-vue-icons/icons";
import axios from "axios";
import { useRouter } from "vue-router";

addIcons(HiSolidUserCircle);

export default {
  props: {
    showMenu: {
      type: Boolean,
      required: true
    }
  },
  setup() {
    const router = useRouter();
    const userData = ref(null);

    const fetchUserProfile = async () => {
      try {
        // Извлекаем токен из localStorage
        const accessToken = localStorage.getItem("access_token");

        if (!accessToken) {
          throw new Error("Токен доступа не найден. Пожалуйста, выполните вход.");
        }

        // Выполняем GET-запрос
        const response = await axios.get("http://172.20.10.3:8000/user/profile", {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });
        // debugger

        // condole.log("AAAAAAAAAAA", name)
        userData.value = response.data;
      } catch (error) {
        console.error("Ошибка при получении профиля:", error);
        alert(error.response?.data?.detail || "Ошибка при получении данных профиля.");
      }
    };

    // Вызываем fetchUserProfile при монтировании компонента
    onMounted(() => {
      fetchUserProfile();
    });

    const goToSearch = () => {
      router.push('/search');
    };

    return {
      userData,
      goToSearch,
    };
  },
};
</script>

<style scoped>
</style>
