<script setup lang="ts">
import { computed, ref } from 'vue'

import ColorPicker from '@components/ColorPicker.vue'
import { Colors } from '@types'
import { AddNewCategory } from '@types'

const name = ref('')
const color = ref<Colors>('fuchsia')

const emits = defineEmits<{
	(event: 'close'): void
	(event: 'submit', payload: AddNewCategory): void
}>()

const touched = ref(false)

function submit(e: Event) {
	e.preventDefault()

	if (name.value.length === 0) {
		onTouch()
		return
	}

	emits('submit', {
		name: name.value,
		color: color.value
	})
}

const allowShowError = computed(() => {
	return touched.value && name.value.length === 0
})

function onTouch() {
	touched.value = true
}

function changeColor(newColor: Colors) {
	color.value = newColor
}
</script>

<template>
	<form
		@submit="submit"
		class="absolute max-w-[300px] shadow rounded-lg px-4 py-4 flex flex-col gap-y-6 border border-black"
	>
		<label class="flex gap-x-2 items-center">
			<div class="text-slate-800">{{ $t('default.name') }}:</div>
			<input
				class="w-full border border-slate-400 px-2 py-1 rounded-md"
				:class="{
					'border-red-400': allowShowError
				}"
				type="text"
				v-model="name"
				@input="onTouch"
			/>
		</label>

		<label class="flex flex-col gap-y-2">
			<ColorPicker
				size="sm"
				:value="color"
				@change="changeColor"
			/>
		</label>

		<div
			v-if="allowShowError"
			class="text-red-600 text-center"
		>
			{{ $t('validation.not-found') }}
		</div>

		<button
			class="w-full bg-green-400 py-2 rounded-md text-white hover:bg-green-500"
		>
			{{ $t('default.add') }}
		</button>
	</form>
</template>
