<template>
	<div id="app" v-if="isHeader">
		<v-app id="inspire">
			<v-app id="keep">
				<v-app-bar
					app
					clipped-left
					color="amber"
				>
					<v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
					<span class="title ml-3 mr-5">MOMOGO&nbsp;
						<!-- <span class="font-weight-light">Keep</span> -->
						</span>
					<v-text-field
						solo-inverted
						flat
						hide-details
						label="Search"

					></v-text-field>
		
					<v-spacer></v-spacer>
				</v-app-bar>
		
				<v-navigation-drawer
					v-model="drawer"
					app
					clipped
					color="grey lighten-4"
				>
					<v-list
						dense
						class="grey lighten-4"
					>
						<template v-for="(item, i) in items">
							<v-row
								v-if="item.heading"
								:key="i"
								align="center"
							>
								<v-col cols="6">
									<v-subheader v-if="item.heading">
										{{ item.heading }}
									</v-subheader>
								</v-col>
								<v-col
									cols="6"
									class="text-right"
								>
									<v-btn
										small
										text
									>edit</v-btn>
								</v-col>
							</v-row>
							<v-divider
								v-else-if="item.divider"
								:key="i"
								dark
								class="my-4"
							></v-divider>
							<v-list-item
								v-else
								:key="i"
								link
							>
								<v-list-item-action>
									<v-icon>{{ item.icon }}</v-icon>
								</v-list-item-action>
								<v-list-item-content>
									<v-list-item-title class="grey--text">
										{{ item.text }}
									</v-list-item-title>
								</v-list-item-content>
							</v-list-item>
						</template>
					</v-list>
				</v-navigation-drawer>
		
				<!-- <v-main>
					<v-container
						fluid
						class="grey lighten-4 fill-height"
					>
						<v-row
							justify="center"
							align="center"
						>
							<v-col class="shrink">
								<v-tooltip right>
									<template v-slot:activator="{ on }">
										<v-btn
											:href="source"
											icon
											large
											target="_blank"
											v-on="on"
										>
											<v-icon large>mdi-code-tags</v-icon>
										</v-btn>
									</template>
									<span>Source</span>
								</v-tooltip>
							</v-col>
						</v-row>
					</v-container>
				</v-main> -->
			</v-app>
		</v-app>
	</div>
</template>

<script>
	import constants from '@/lib/constants.js'


	export default {
		name: 'Header',
		components: {

		},
		props: [
			'isHeader'
		],
		computed: {
		},
		watch: {
		},
		created: {
		},
		methods: {
		},
		data: function() {
			return {
				constants,
				drawer: null,
				items: [
					{text: '식단달력' },
					{text: '커뮤니티' },
					{ divider: true },
					// { heading: 'Labels' },
					{ text: '마이페이지' },
					{ divider: true },
					{text: '추천' },
					{text: '위시리스트' },
					{ divider: true },
					{text: '밥류' },
					{text: '구이류' },
					{text: '국류' },
					{text: '반찬류' },
					{text: '기타' },
				]
			}
		}
		
	}
</script>


<style>
	#keep .v-navigation-drawer__border {
		display: none
	}
</style>