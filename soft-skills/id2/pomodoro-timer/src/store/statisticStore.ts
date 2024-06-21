import { defineStore } from 'pinia'

import { AddNewStatistic, Statistic } from '@types'

interface StatisticStore {
	statistic: Statistic[]
}

export const useStatistic = defineStore('statistic', {
	state: (): StatisticStore => ({
		statistic: []
	}),

	actions: {
		add(payload: AddNewStatistic) {
			this.statistic.push({
				_id: String(new Date(Date.now())),
				date: String(new Date(Date.now() - payload.count)),
				count: payload.count,
				mode: payload.mode,
				category: payload.category
			})
		},
		delete(statisticItem: Statistic) {
			this.statistic = this.statistic.filter(
				item => item._id !== statisticItem._id
			)
		}
	},

	persist: true
})
