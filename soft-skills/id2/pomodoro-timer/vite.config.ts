import vue from '@vitejs/plugin-vue'
import path from 'path'
import { defineConfig } from 'vite'
import svgLoader from 'vite-svg-loader'

export default defineConfig({
	resolve: {
		alias: {
			'@assets': path.resolve(__dirname, './src/assets'),
			'@components': path.resolve(__dirname, './src/components'),
			'@constants': path.resolve(__dirname, './src/constants'),
			'@pages': path.resolve(__dirname, './src/pages'),
			'@store': path.resolve(__dirname, './src/store'),
			'@types': path.resolve(__dirname, './src/types'),
			'@utils': path.resolve(__dirname, './src/utils'),
			'@directives': path.resolve(__dirname, './src/directives'),
			'@': path.resolve(__dirname, './src')
		}
	},
	plugins: [
		vue(),
		svgLoader({
			defaultImport: 'component'
		})
	]
})
