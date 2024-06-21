import { Colors } from '.'

export interface Category {
	_id: string
	name: string
	mode: 'number' | 'time' // Тільки time, number для помідорок не потрібен
	// comment: string
	color: Colors
	// order: number // Подивимось) Не буде використанно в цій версії
	// dimension?: string // Не буде використанно в цій версії
	// group: string[] // Не буде використанно в цій версії
	// archived: boolean // Подивимось) Не буде використанно в цій версії
	// trash: boolean // Подивимось) Не буде використанно в цій версії
	// trash_expires: number // Подивимось) Не буде використанно в цій версії
}
