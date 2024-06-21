<script setup lang="ts">
import { computed, ref } from 'vue'

import tailwindColors from 'tailwindcss/colors'

import BedIcon from '@assets/icons/bed.svg'
import BrainIcon from '@assets/icons/brain.svg'
import CupIcon from '@assets/icons/cup.svg'
import { Colors, Mode, ModeItem } from '@types'

const props = defineProps<{
	modelValue: Mode
	colors: Record<Mode, Colors>
}>()

const emit = defineEmits<{
	(e: 'update:modelValue', value: Mode): void
}>()

const selectedColor = computed({
	get() {
		const findedItem = colorsData.find(item => item.id === props.modelValue)
		return findedItem || colorsData[0]
	},
	set(value) {
		emit('update:modelValue', value.id)
	}
})

const colorsData: ModeItem[] = [
	{
		id: Mode.pomodoro,
		title: 'Focus',
		icon: BrainIcon
	},
	{
		id: Mode.short,
		title: 'Short break',
		icon: CupIcon
	},
	{
		id: Mode.long,
		title: 'Long break',
		icon: BedIcon
	}
]

function hideSelect() {
	selectOpen.value = false
}

function toggleSelect() {
	selectOpen.value = !selectOpen.value
}

const selectOpen = ref(false)

function changeSelectedColor(data: ModeItem) {
	selectedColor.value = data
	selectOpen.value = false
}
</script>

<template>
	<div
		class="relative whitespace-nowrap"
		v-close-modal="hideSelect"
	>
		<button
			class="item-colors rounded-full border flex items-center gap-x-2 px-4 py-2 item-colors-selected cursor-pointer transition-all duration-100"
			:style="{
				'--select-mode-bg':
					tailwindColors[props.colors[selectedColor.id]]['100'],
				'--select-mode-border-color':
					tailwindColors[props.colors[selectedColor.id]]['950'],
				'--select-mode-color':
					tailwindColors[props.colors[selectedColor.id]]['950'],
				'--select-mode-bg-hover':
					tailwindColors[props.colors[selectedColor.id]]['200'],
				'--select-mode-selected-border-color':
					tailwindColors[props.colors[selectedColor.id]]['950']
			}"
			@click="toggleSelect"
		>
			<component
				:is="selectedColor.icon"
				class="w-6 h-6"
			/>
			{{ selectedColor.title }}
		</button>

		<div
			v-if="selectOpen"
			class="absolute top-10 mt-2 flex flex-col rounded-xl overflow-hidden border border-black z-10"
		>
			<button
				v-for="item in colorsData"
				:key="item.title"
				class="item-colors flex items-center gap-x-2 px-4 py-2 cursor-pointer transition-all duration-100"
				@click="changeSelectedColor(item)"
				:style="{
					'--select-mode-bg': tailwindColors[props.colors[item.id]]['100'],
					'--select-mode-border-color':
						tailwindColors[props.colors[item.id]]['950'],
					'--select-mode-color': tailwindColors[props.colors[item.id]]['950'],
					'--select-mode-bg-hover':
						tailwindColors[props.colors[item.id]]['200'],
					'--select-mode-selected-border-color':
						tailwindColors[props.colors[item.id]]['950']
				}"
			>
				<component
					:is="item.icon"
					class="w-6 h-6"
				></component>

				{{ item.title }}
			</button>
		</div>
	</div>
</template>

<style scoped>
.item-colors {
	background: var(--select-mode-bg);
	border-color: var(--select-mode-border-color);
	color: var(--select-mode-color);
}

.item-colors:hover {
	background: var(--select-mode-bg-hover);
}

.item-colors-selected {
	border-color: var(--select-mode-selected-border-color);
}
</style>
