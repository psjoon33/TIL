<template>

	<div id="graph">
		<v-app id="inspire">
			<v-simple-table>
				<template v-slot:default>
					<thead>
						<tr>
							<th class="text-left" style="border-top:1px solid black; font-size:1em;">
								항목
							</th>
							<th class="text-left" style="border-top:1px solid black; border-left:1px solid grey; border-right:1px solid gray; font-size:1em;">
								1일권장량
							</th>
							<th class="text-left" style="border-top:1px solid black; font-size:1em;">
								섭취량
							</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td class="text-left">
								열량
							</td>
							<td class="text-left" style="border-left:1px solid grey; border-right:1px solid gray">
								0
							</td>
							<td class="text-left">
								0
							</td>
						</tr>
						<tr>
							<td class="text-left">
								탄수화물
							</td>
							<td class="text-left" style="border-left:1px solid grey; border-right:1px solid gray">
								0
							</td>
							<td class="text-left">
								0
							</td>
						</tr>
						<tr>
							<td class="text-left">
								단백질
							</td>
							<td class="text-left" style="border-left:1px solid grey; border-right:1px solid gray">
								0
							</td>
							<td class="text-left">
								0
							</td>
						</tr>
						<tr>
							<td class="text-left">
								지방
							</td>
							<td class="text-left" style="border-left:1px solid grey; border-right:1px solid gray">
								0
							</td>
							<td class="text-left">
								0
							</td>
						</tr>

					</tbody>
				</template>
			</v-simple-table>
		</v-app>
	</div>
</template>



<script>
import LineChart from "@/components/LineChart";

export default {
  name: "VueChartJS",
  data() {
    return {

    }
  },
  components: {
    LineChart,
  },
  mounted() {

  },
  methods: {

  },
};
</script>


<style scoped>
  td {
    height: 9vh !important;
  }

  .title {
    justify-content: center;
    text-align: center;
    font-size: 1.4em;
  }

</style>