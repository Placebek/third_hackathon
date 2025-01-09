import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default {
  plugins: [vue()],
  server: {
    host: '172.20.10.8',  
    port: 3000,       
  },
};