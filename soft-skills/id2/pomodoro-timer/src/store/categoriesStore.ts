import { defineStore } from 'pinia'

import { AddNewCategory, Category } from '@types'

interface CategoryStore {
	categories: Category[]
}

export const useCategoryStore = defineStore('category', {
	state: (): CategoryStore => ({
		// TODO: Refactor
		categories: [
			{
				_id: '0',
				color: 'gray',
				mode: 'time',
				name: 'Default'
			}
		]
	}),

	actions: {
		add(payload: AddNewCategory) {
			this.categories.push({
				_id: String(new Date(Date.now()).getTime()),
				mode: 'time',
				...payload
			})
		},

		delete(categoriesItem: Category) {
			this.categories = this.categories.filter(
				item => item._id !== categoriesItem._id
			)
		}
	},

	persist: true
})
