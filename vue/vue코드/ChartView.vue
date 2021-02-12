<template>
  <section class="container">
    <div class="columns">
      <div class="column" style="margin-left: 50px; margin-top: 100px">
        <div style="width: 30vw; height: 50vh">
          <p
            style="
              justify-content: center;
              text-align: center;
              font-size: 1.2em;
            "
          >
            박성준님의 일주일간 칼로리 섭취 추이
          </p>
          <line-chart
            style="width: 30vw; height: 40vh; min-height: 20px !important"
          ></line-chart>
        </div>
      </div>
    </div>
  </section>
</template>



<script>
import LineChart from "@/components/LineChart";

export default {
  name: "VueChartJS",
  components: {
    LineChart,
  },
};
</script>
