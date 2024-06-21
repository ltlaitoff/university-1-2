<script setup lang="ts">
import tailwindColors from 'tailwindcss/colors'

import LeftPanel from '@components/LeftPanel/LeftPanel.vue'
import HomePage from '@pages/HomePage.vue'
import { useUserSettingsStore } from '@store/userSettingsStore'

const userSettings = useUserSettingsStore()
</script>

<template>
	<main class="main font-['Roboto'] w-full h-full min-h-screen pb-[15vh]">
		<LeftPanel />

		<div class="min-h-full flex items-center justify-center">
			<HomePage />
		</div>
	</main>
</template>

<style scoped>
.main {
	background: v-bind(
		'tailwindColors[userSettings.colors[userSettings.settings.selectedMode]]["50"]'
	);
}
</style>
