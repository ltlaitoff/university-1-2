<script setup lang="ts">
import { computed, withDefaults } from 'vue'

import MinusIcon from '@assets/icons/minus.svg'
import PlusIcon from '@assets/icons/plus.svg'

const props = withDefaults(
	defineProps<{
		modelValue: number
		min?: number
		max?: number
	}>(),
	{
		min: 0,
		max: 1000
	}
)

const emits = defineEmits<{
	(event: 'update:modelValue', value: number): void
}>()

const inputValue = computed({
	get() {
		return props.modelValue
	},
	set(value) {
		emits('update:modelValue', validateValue(value))
	}
})

const increment = () => {
	inputValue.value = props.modelValue + 1
}

const decrement = () => {
	inputValue.value = props.modelValue - 1
}

const validateValue = (value: number) => {
	if (props.min != undefined && value < props.min) return props.min
	if (props.max != undefined && value > props.max) return props.max

	return value
}
</script>

<template>
	<div class="flex gap-x-2">
		<button
			class="p-2 bg-slate-200 rounded-xl text-slate-700 hover:bg-slate-300"
			@click="decrement"
		>
			<MinusIcon class="w-4 h-4" />
		</button>

		<input
			class="border border-slate-400 px-2 py-1 rounded-xl"
			type="number"
			:min="props.min"
			:max="props.max"
			v-model="inputValue"
		/>

		<button
			class="p-2 bg-slate-200 rounded-xl text-slate-700 hover:bg-slate-300"
			@click="increment"
		>
			<PlusIcon class="w-4 h-4" />
		</button>
	</div>
</template>

<style scoped></style>
