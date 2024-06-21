<script setup lang="ts">
import ColorPicker from '@components/ColorPicker.vue'
import ModeShild from '@components/ModeShild.vue'
import NumberInput from '@components/NumberInput.vue'
import { useUserSettingsStore } from '@store/userSettingsStore'
import { Mode } from '@types'

const userSettings = useUserSettingsStore()

const modes: Mode[] = Object.values(Mode) as Mode[]
</script>

<template>
	<div
		class="pl-6 pr-6 py-6 w-[450px] max-md:pb-6 max-md:w-full h-full flex flex-col gap-y-2 overflow-y-scroll"
	>
		<div class="text-center text-2xl">{{ $t('settings.title') }}</div>

		<div class="flex flex-col gap-y-10">
			<div class="flex flex-col gap-y-10">
				<div
					class="flex flex-col gap-y-4"
					v-for="mode of modes"
					:key="mode"
				>
					<ModeShild :mode="mode" />

					<NumberInput
						class="ml-1"
						v-model="userSettings.settings.times[mode]"
						:max="1439"
						:min="1"
					/>

					<ColorPicker
						class="ml-1"
						:value="userSettings.colors[mode]"
						@change="value => userSettings.setColor(mode, value)"
					/>
				</div>
				<div class="">
					<div class="px-4 text-lg">Approaches count:</div>
					<NumberInput
						class="ml-1 mt-1"
						v-model="userSettings.settings.approachesCount"
						:max="100"
						:min="1"
					/>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped></style>
