<template>
  <div class="bg-[#1c1c1c] rounded-lg">
    SSSSSSSSSSS
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