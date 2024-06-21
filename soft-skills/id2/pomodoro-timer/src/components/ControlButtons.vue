<script setup lang="ts">
import tailwindColors from 'tailwindcss/colors'

import FastForwardIcon from '@assets/icons/fastForward.svg'
import PauseIcon from '@assets/icons/pause.svg'
import PlayIcon from '@assets/icons/play.svg'
import StopIcon from '@assets/icons/stop.svg'
import { Colors } from '@types'

const props = defineProps<{
	isRunning: boolean
	color: Colors
}>()

const emits = defineEmits<{
	(e: 'stop'): void
	(e: 'fastForward'): void
	(e: 'playOrPause'): void
}>()
</script>

<template>
	<div class="flex justify-center items-center gap-x-2">
		<div class="">
			<button
				@click="emits('stop')"
				class="secondary-button inline text-lg px-4 py-4 rounded-2xl hover:shadow transition-all duration-200"
			>
				<StopIcon class="w-5 h-5" />
			</button>
		</div>

		<div class="">
			<button
				@click="emits('playOrPause')"
				class="primary-button inline text-lg px-6 py-4 rounded-2xl hover:shadow transition-all duration-200"
			>
				<PlayIcon
					v-if="!props.isRunning"
					class="w-7 h-7"
				/>
				<PauseIcon
					v-else
					class="w-7 h-7"
				/>
			</button>
		</div>

		<div class="">
			<button
				@click="emits('fastForward')"
				class="secondary-button inline text-lg px-4 py-4 rounded-2xl hover:shadow transition-all duration-200"
			>
				<FastForwardIcon class="w-5 h-5" />
			</button>
		</div>
	</div>
</template>

<style scoped>
.primary-button {
	background: v-bind("tailwindColors[props.color]?.['400']");
	color: v-bind("tailwindColors[props.color]?.['950']");
}

.primary-button:hover {
	background: v-bind("tailwindColors[props.color]?.['500']");
}

.secondary-button {
	background: v-bind("tailwindColors[props.color]?.['200']");
	color: v-bind("tailwindColors[props.color]?.['900']");
}

.secondary-button:hover {
	background: v-bind("tailwindColors[props.color]?.['300']");
}
</style>
