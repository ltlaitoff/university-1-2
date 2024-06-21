import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'

import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import { vCloseModal } from '@directives'

import App from './App.vue'
import enTranslation from './assets/i18n/en/translation.json'
import './style.css'

const app = createApp(App)
const pinia = createPinia()
const i18n = createI18n({
	locale: 'en',
	messages: {
		en: enTranslation
	}
})

pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(i18n)

app.directive('close-modal', vCloseModal)

app.mount('#app')
