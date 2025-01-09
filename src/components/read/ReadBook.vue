<template>
  <div class="w-full h-screen">
    <Navbar />
    <div>
      <div class="flex items-center justify-center mt-12 p-2 text-white">
        <div class="flex items-center flex-col text-center gap-2 p-2">
          <div class="text-2xl">
              PUSS IN POOTS
            </div>
            <div class="text-xl">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea neque nisi deserunt, quos accusantium ullam
            </div>
          <div class="text-justify mt-5 text-lg indent-8">
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci nemo velit eveniet quia sequi, reiciendis magni, provident laborum quod officia nobis. Odit vel libero minima, ipsa ducimus aut quibusdam veritatis.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero nostrum, dignissimos perferendis porro, a quisquam ipsam expedita quasi dolorum adipisci provident. Illo quidem nesciunt, beatae vel quae quas? Assumenda, eum!</p>
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero nostrum, dignissimos perferendis porro, a quisquam ipsam expedita quasi dolorum adipisci provident. Illo quidem nesciunt, beatae vel quae quas? Assumenda, eum!</p>
          </div>
        </div>
      </div>
    </div>
    <FootMenu />
  </div>
</template>

<script>
import { ref } from "vue";
import { addIcons } from "oh-vue-icons";
import Navbar from "../menu/Navbar.vue";
import FootMenu from "../read/FootMenu.vue";

export default {
  name: "ReadBook",
  components: {
    Navbar,
    FootMenu
  },
};
</script>

<style scoped>
</style>
