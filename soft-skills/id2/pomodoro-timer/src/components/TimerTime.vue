<script setup lang="ts">
import TimerDigit from './TimerDigit.vue'

const props = defineProps<{
	hours: number
	minutes: number
	seconds: number
}>()
</script>

<template>
	<div
		class="text-center mt-6 text-[8rem] max-md:text-[4rem] leading-[0.8] flex items-center"
	>
		<TimerDigit
			v-if="props.hours > 0"
			:digit="props.hours"
		/>
		<span v-if="props.hours > 0">:</span>
		<TimerDigit :digit="props.minutes" />
		<span>:</span>
		<TimerDigit :digit="props.seconds" />
	</div>
</template>
