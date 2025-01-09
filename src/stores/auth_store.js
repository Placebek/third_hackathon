import { defineStore } from 'pinia';
import { fetchWrapper } from './fetch';
import { useRouter } from 'vue-router'; // Импортируем useRouter

const baseUrl = `${import.meta.env.BASE_URL}/`;

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')),
    returnUrl: null,
  }),
  actions: {
    async login(email, password) {
      const router = useRouter(); // Инициализируем router
      try {
        const user = await fetchWrapper.post(`${baseUrl}`, { email, password });

        this.user = user;
        localStorage.setItem('user', JSON.stringify(user));

        router.push(this.returnUrl || '/'); // Перенаправляем после успешного логина
      } catch (error) {
        console.error('Login error:', error);
        // Здесь можно добавить логику для отображения ошибок в UI
      }
    },
    logout() {
      this.user = null;
      localStorage.removeItem('user');

      const router = useRouter();
      router.push('/login');
    },
  },
});
