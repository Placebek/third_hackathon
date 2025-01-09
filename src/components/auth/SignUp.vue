<template>
  <div class="h-screen bg-[#14161B] overflow-hidden relative">
    <div class="container h-screen flex items-center justify-center px-8 mx-auto">
      <div class="bg-white h-[460px] w-[320px] rounded-lg relative p-7 shadow-lg shadow-cyan-200/20">
        <form class="flex flex-col items-center mt-4 h-screen">
          <h4 class="text-2xl font-semibold mb-7 text-center">SignUp</h4>

          <input
            type="text"
            placeholder="Email"
            class="input-box"
          />
          <input
            type="text"
            placeholder="Username"
            class="input-box"
          />
          <input
            type="password"
            placeholder="Password"
            class="input-box"
          />
          
          <button 
            type="submit" 
            class="btn-login-f"
          >
          SIGNUP
          </button>

          <!-- <router-link to="/signUp" class="btn-login-f">
            SIGNUP
          </router-link> -->

          <p class="text-xs text-slate-500 text-center my-4">Or</p>

          <!-- <button
            type="button"
            class="btn-login-s"
          > -->
          <button 
            to="/signUp" 
            class="btn-login-s"
            @click="goToLogin"
          >
            LOGIN TO ACCOUNT
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpForm',
  methods: {
    goToLogin() {
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
</style>