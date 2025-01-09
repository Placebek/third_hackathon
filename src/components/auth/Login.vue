<template>
  <div class="h-screen bg-[#14161B] overflow-hidden relative">
    <div class="container h-screen flex items-center justify-center px-8 mx-auto">
      <div class="bg-white h-[420px] w-[320px] rounded-lg relative p-7 shadow-lg shadow-cyan-200/20">
        <Form @submit="handleLogin" :validation-schema="schema">
          <div class="flex flex-col items-center mt-4 h-screen">
            <h4 class="text-2xl font-semibold mb-7 text-center">Login</h4>
            
            <div class="w-full">
              <div class="form-group">
                <Field 
                  name="email" 
                  type="text" 
                  placeholder="Email" 
                  class="input-box"
                />
                <ErrorMessage name="email" class="text-red-500 text-xs mt-1" />
              </div>
              <div class="form-group mt-4">
                <Field 
                  name="password" 
                  type="password" 
                  placeholder="Password" 
                  class="input-box"
                />
                <ErrorMessage name="password" class="text-red-500 text-xs mt-1" />
              </div>
            </div>
            
            <button 
              type="submit" 
              class="btn-login-f"
            >
            LOGIN
            </button>

            <p class="text-xs text-slate-500 text-center my-4">Or</p>

            <button 
              to="/" 
              class="btn-login-s"
              @click="goToSignUp"
            >
            CREATE ACCOUNT
            </button>
            <div class="form-group">
              <div v-if="message" class="alert alert-danger" role="alert">
                {{ message }}
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
import { useAuthStore } from "../../stores/auth_store.js";

export default {
  name: 'LoginForm',
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
      username: yup.string().required("Username is required!"),
      password: yup.string().required("Password is required!"),
    });

    return {
      loading: false,
      message: "",
      schema,
    };
  },
  computed: {
    loggedIn() {
      const authStore = useAuthStore();
      return authStore.user !== null;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/dashboard");
    }
  },
  methods: {
    goToSignUp() {
      this.$router.push('/signUp');
    },

    handleLogin(user) {
      this.loading = true;

      this.$store.dispatch("auth/login", user).then(
        () => {
          this.$router.push("/dashboard");
        },
        (error) => {
          this.loading = false;
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        }
      );
    },
  },
};
</script>

<style scoped>
</style>