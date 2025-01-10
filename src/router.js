import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from './components/auth/Login.vue'; 
import SignUpForm from './components/auth/SignUp.vue';
import DashboardForm from './components/dashboard/Dashboard.vue';
import MainBook from './components/book/MainBook.vue';
import Settings from './components/settings/Settings.vue';
import ReadBook from './components/read/ReadBook.vue';
import SearchForm from './components/menu/Search.vue';
import BookPage from './components/read/BookPage.vue';


const routes = [
  {
    path: '/login',
    name: 'LoginForm',
    component: LoginForm,
  },
  {
    path: '/signup',
    name: 'SignUpForm',
    component: SignUpForm,
  },
  {
    path: '/dashboard',
    name: 'DashboardForm',
    component: DashboardForm,
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings,
  },
  {
    path: '/readbook',
    name: 'ReadBook',
    component: ReadBook,
  },
  {
    path: '/search',
    name: 'SearchForm',
    component: SearchForm,
  },
  {
    path: '/bookpage',
    name: 'BookPage',
    component: BookPage,
  },
  { 
    path: '/mainbook/:id', 
    name: 'MainBook', 
    component: MainBook 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
