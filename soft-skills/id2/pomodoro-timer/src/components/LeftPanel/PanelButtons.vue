<script setup lang="ts">
import tailwindColors from 'tailwindcss/colors'

import { LeftPanelModes } from '@types'

import { useUserSettingsStore } from '../../store/userSettingsStore'

const props = defineProps<{
	isOpened: boolean
	mode: LeftPanelModes
	burgerOpened: boolean
}>()

const emits = defineEmits<{
	(event: 'click', value: LeftPanelModes): void
	(event: 'burgerToggle'): void
}>()

const userSettings = useUserSettingsStore()

const data: {
	title: string
	key: LeftPanelModes
}[] = [
	{
		title: 'Settings',
		key: 'settings'
	},
	{
		title: 'Categories',
		key: 'category'
	},
	{
		title: 'Statistic',
		key: 'statistic'
	}
]
</script>

<template>
	<div class="pt-10 h-full flex flex-col justify-start gap-y-2 max-md:hidden">
		<button
			v-for="item of data"
			:key="item.key"
			class="py-3 px-4 rounded-r-xl shadow clip-your-needful-style text-[--right-panel-color-950]"
			:class="
				props.isOpened === false
					? 'bg-[--right-panel-color-200]'
					: props.mode === item.key
					? 'bg-[--right-panel-color-300] z-20'
					: 'bg-[--right-panel-color-200]'
			"
			@click="emits('click', item.key)"
		>
			{{ item.title }}
		</button>
	</div>

	<div class="max-md:flex hidden z-10">
		<button
			class="absolute top-5 right-5 w-8 h-8 bg-[--button-panel-bg] rounded-lg z-50 flex items-center justify-center"
			:class="props.burgerOpened ? 'gap-y-[0px]' : 'gap-y-[5px]'"
			:style="{
				'--button-panel-bg':
					tailwindColors[userSettings.colors[userSettings.selectedMode]]['300']
			}"
			@click="emits('burgerToggle')"
		>
			<div class="flex flex-col gap-y-[3px]">
				<div
					class="bg-black w-[15px] h-[2px] rounded-full"
					:class="props.burgerOpened ? ' rotate-45' : 'rotate-0'"
				></div>
				<div
					class="bg-black w-[15px] h-[2px] rounded-full"
					:class="props.burgerOpened ? 'hidden' : ''"
				></div>
				<div
					class="bg-black w-[15px] h-[2px] rounded-full"
					:class="props.burgerOpened ? '-mt-[5px] -rotate-45' : 'rotate-0'"
				></div>
			</div>
		</button>

		<div
			class="absolute min-w-[100vw] w-full h-full bg-white flex items-center justify-center flex-col"
			:class="props.burgerOpened ? 'top-0' : '-top-full'"
		>
			<button
				v-for="item of data"
				:key="item.key"
				class="py-6 px-4 text-[--right-panel-color-950] hover:bg-slate-200 rounded-md transition-all duration-150 text-2xl w-full"
				@click="emits('click', item.key)"
			>
				{{ item.title }}
			</button>
		</div>
	</div>
</template>
