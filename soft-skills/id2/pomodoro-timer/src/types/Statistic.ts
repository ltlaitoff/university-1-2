import { Category } from '.'
import { Mode } from './Mode'

export interface Statistic {
	_id: string
	date: string // Date as ISO string
	mode: Mode // Lapricot diff
	count: number
	// comment: string
	category: Category
}
