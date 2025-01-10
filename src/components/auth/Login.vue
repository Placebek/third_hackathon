<template>
  <div class="h-screen bg-[#14161B] overflow-hidden relative">
    <div class="container h-screen flex items-center justify-center px-8 mx-auto">
      <div class="bg-white h-[420px] w-[320px] rounded-lg relative p-5 shadow-lg shadow-cyan-200/20">
        <Form :validation-schema="schema" @submit="handleLogin">
          <div class="flex flex-col items-center mt-4 h-screen">
            <h4 class="text-2xl font-semibold mb-4 text-center">Login</h4>
            
            <div class="w-full">
              <div class="form-group">
                <Field 
                  name="email_or_username"
                  type="email"
                  v-model="email_or_username"
                  placeholder="Email" 
                  class="input-box"
                  :class="{'is-invalid': errors?.email_or_username}"
                />
                <!-- <ErrorMessage name="email_or_username" class="is-invalid " /> -->
              </div>
              <div class="form-group mt-2">
                <Field 
                  name="password" 
                  type="password" 
                  placeholder="Password" 
                  class="input-box"
                  v-model="password"
                  :class="{'is-invalid': errors?.password}"
                />
                <!-- <ErrorMessage name="password" class="is-invalid " /> -->
              </div>
            </div>

            <div v-if="message" class="error-message mb-3">{{ message }}</div>
            
            <div class="w-full">
              <div>
                <button 
                  type="submit" 
                  class="btn-login-f"
                >
                LOGIN
                </button>
              </div>

              <p class="text-xs text-slate-500 text-center my-4">Or</p>

              <button 
                to="/" 
                class="btn-login-s"
                @click="goToSignUp"
              >
              CREATE ACCOUNT
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { Form, Field, ErrorMessage, useForm, useField } from "vee-validate";
import * as yup from "yup";
import axios from "axios";
import { ref } from "vue";
import { useRouter } from 'vue-router';

export default {
  name: "Login",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  setup() {
    // Создаем роутер с помощью useRouter
    const router = useRouter();

    // Состояние для загрузки
    const loading = ref(false);
    const message = ref("");

    // Определяем схему валидации с помощью yup
    const schema = yup.object().shape({
      email_or_username: yup
        .string()
        .required("Email or Username is required!"),
      password: yup.string().required("Password is required!"),
    });

    // useForm хук для валидации формы
    const { errors, handleSubmit, reset } = useForm({
      validationSchema: schema,
    });

    // useField для каждого поля
    const { value: email_or_username } = useField("email_or_username");
    const { value: password } = useField("password");

    const handleLogin = async (values) => {
      loading.value = true;
      message.value = "";

      try {
        // Изменили объект для отправки правильных параметров
        const response = await axios.post("http://172.20.10.3:8000/auth/login", {
          email_or_username: values.email_or_username, // Передаем email_or_username
          password: values.password, // Передаем password
        });

        const accessToken = response.data.access_token;
        const access_token_type = response.data.access_token_type;

        if (accessToken) {
          localStorage.setItem("access_token", accessToken);
          localStorage.setItem("access_token_type", access_token_type);
        } else {
          console.error("Токен не найден в ответе сервера");
        }

        router.push("/dashboard"); 
      } catch (error) {
        loading.value = false;
        console.log("Login error:", error);
        message.value =
          (error.response &&
            error.response.data &&
            error.response.data.message) ||
          error.message ||
          error.toString();
      }
    };

    const goToSignUp = () => {
      router.push('/signup'); // Переходим на страницу регистрации
    };

    return {
      email_or_username,  // Используем новое поле для email_or_username
      password,
      schema,
      errors,
      handleLogin,
      loading,
      message,
      goToSignUp,
    };
  },
};
</script>

<style scoped>
.is-invalid {
  border-color: red;
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>