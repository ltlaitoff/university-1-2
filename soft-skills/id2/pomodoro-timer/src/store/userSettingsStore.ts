import { defineStore } from 'pinia'

import { approachesLimits } from '@constants/approachesLimits'
import { Category, Colors, Mode } from '@types'

interface UserSettingsStore {
	settings: {
		colors: Record<Mode, Colors>
		times: Record<Mode, number>
		selectedMode: Mode
		selectedCategory: Category
		approachesCount: number
	}
	currentApproach: number
	activeCompletedPomodoro: boolean
}

export const useUserSettingsStore = defineStore('settings', {
	state(): UserSettingsStore {
		return {
			settings: {
				colors: {
					[Mode.pomodoro]: 'blue',
					[Mode.short]: 'purple',
					[Mode.long]: 'red'
				},
				times: {
					[Mode.pomodoro]: 25,
					[Mode.short]: 5,
					[Mode.long]: 15
				},
				selectedMode: Mode.pomodoro,
				selectedCategory: {
					_id: '0',
					color: 'red',
					mode: 'time',
					name: 'Pomodoro'
				},
				approachesCount: 4
			},
			currentApproach: 1,
			activeCompletedPomodoro: false
		}
	},
	getters: {
		colors: state => state.settings.colors,
		times: state => state.settings.times,
		selectedMode: state => state.settings.selectedMode
	},
	actions: {
		setColor(mode: Mode, color: Colors) {
			this.settings.colors[mode] = color
		},
		setSelectedMode(mode: Mode) {
			this.settings.selectedMode = mode
		},
		setApproachesCount(value: number) {
			if (value > approachesLimits.max || value < approachesLimits.min) return

			this.settings.approachesCount = value
		}
	},
	persist: true
})
