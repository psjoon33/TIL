<script>
//Importing Line class from the vue-chartjs wrapper
import { Line } from "vue-chartjs";
//Exporting this so it can be used in other components
export default {
  extends: Line,
  data() {
    return {
      datacollection: {
        //Data to be represented on x-axis
        labels: ["D-7", "D-6", "D-5", "D-4", "D-3", "D-2", "D-1"],
        datasets: [
          {
            label: "칼로리 섭취량",
            backgroundColor: "white",
            pointBackgroundColor: "white",
            borderWidth: 10,
            pointBorderColor: "black",
            //Data to be represented on y-axis
            data: [40, 20, 30, 50, 90, 30, 60],
            // padding-left: '20px'
          },
        ],
      },
      //Chart.js options that controls the appearance of the chart
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
                padding: 50,
              },
              gridLines: {
                display: false,
              },
            },
          ],
          xAxes: [
            {
              gridLines: {
                display: false,
              },
            },
          ],
        },
        legend: {
          display: true,
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  mounted() {
    //renderChart function renders the chart with the datacollection and options object.
    this.renderChart(this.datacollection, this.options);
  },
};
</script>
