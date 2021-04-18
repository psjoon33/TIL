<template>
  <vue-scroll-snap :fullscreen="true">
    <div class="item" id="one"></div>
    <div class="item" id="two"></div>
    <div class="item" id="three"></div>
    <div class="item" id="four"></div>
  </vue-scroll-snap>
</template>

<script>
import VueScrollSnap from "vue-scroll-snap";

export default {
  name: "FullscreenVertical",
  components: { VueScrollSnap },
  data() {
    return {
      windowTop: window.top.scrollY,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
    onScroll(e) {
      this.windowTop = e.target.scrollTop;
      console.log(this.windowTop);
    },
  },
};
</script>
