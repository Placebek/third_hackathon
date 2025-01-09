<template>
  <div class="h-screen bg-[#14161B] overflow-hidden relative">
    <div class="container h-screen flex items-center justify-center px-8 mx-auto">
      <div class="bg-white h-[420px] w-[320px] rounded-lg relative p-7 shadow-lg shadow-cyan-200/20">
        <form class="flex flex-col items-center mt-4 h-screen">
          <h4 class="text-2xl font-semibold mb-7 text-center">Login</h4>

          <input
            type="text"
            placeholder="Email"
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
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  methods: {
    goToSignUp() {
      this.$router.push('/signUp');
    }
  }
};
</script>

<style scoped>
</style>