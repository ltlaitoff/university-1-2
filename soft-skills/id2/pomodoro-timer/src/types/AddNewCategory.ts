import { Category } from '.'

export type AddNewCategory = Omit<Category, '_id' | 'mode'>
