<template>
    <div class="bg-[#1c1c1c] rounded-lg">
      <div class="flex items-center p-3">
        <div class="flex flex-col space-y-2">
          <div class="flex flex-row itmes-start">
            <div class="w-1/2">Author name:</div>
            <div class="w-1/2">{{ storyData.author_name }}</div>
          </div>
          
          <!-- Вторая строка -->
          <div class="flex flex-row itmes-start">
            <div class="w-1/2">Age category:</div>
            <div class="w-1/2">{{ storyData.age_category }}</div>
          </div>
          
          <!-- Третья строка -->
          <div class="flex flex-row itmes-start">
            <div class="w-1/2">Popularity:</div>
            <div class="w-1/2">10</div>
          </div>
          
          <!-- Четвертая строка -->
          <div class="flex flex-row itmes-start">
            <div class="w-1/2">Readers:</div>
            <div class="w-1/2">{{ storyData.story_reads }}</div>
          </div>
        </div>
      </div>
      <div class="pl-8 font-bold text-2xl text-[#ae87e0]">
        Prologue
      </div>
      <div class="p-5 text-justify indent-8">
        <div class="text-md">
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium adipisci, maiores enim aliquam facere quos dolores recusandae rem, aliquid architecto molestias repellendus assumenda deserunt, repellat hic eligendi exercitationem excepturi eos!
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium adipisci, maiores enim aliquam facere quos dolores recusandae rem, </p>
          <p>Aliquid architecto molestias repellendus assumenda deserunt, repellat hic eligendi exercitationem excepturi eos!</p>
        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    storyId: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      storyData: {},
    };
  },
  mounted() {
    axios
      .get(`http://172.20.10.3:8000/user/stories/${this.storyId}`)
      .then((response) => {
        this.storyData = response.data;
      })
      .catch((error) => {
        console.error("Error fetching story data:", error);
      });
  },
};
</script>

<style scoped>

</style>