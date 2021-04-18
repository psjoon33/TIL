<template>
  <vue-scroll-snap :fullscreen="true" :horizontal="true">
    <div class="item" id="one"></div>
    <div class="item" id="two">asdfadsf</div>
    <div class="item" id="three">asdfdasf</div>
    <div class="item" id="four">asdfasd</div>
  </vue-scroll-snap>
</template>

<script>
import VueScrollSnap from "vue-scroll-snap";

export default {
  name: "FullscreenHorizontal",
  components: { VueScrollSnap },
  data() {
    return {};
  },
  methods: {
    findy() {
      console.log(window.scrollY);
    },
  },
};
</script>
