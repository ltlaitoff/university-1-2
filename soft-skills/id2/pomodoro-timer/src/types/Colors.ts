import type { DefaultColors } from 'tailwindcss/types/generated/colors'

export type Colors = keyof Omit<
	DefaultColors,
	'inherit' | 'current' | 'transparent' | 'black' | 'white'
>
