<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
	digit: number
}>()

const stringDigit = computed(() => {
	const digit = props.digit

	if (digit >= 10) return String(digit)

	return '0' + String(digit)
})
</script>

<template>
	<span>
		{{ stringDigit }}
	</span>
</template>
