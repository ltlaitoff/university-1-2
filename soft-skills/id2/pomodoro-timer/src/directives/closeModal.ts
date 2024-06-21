import { ObjectDirective } from 'vue'

// eslint-disable-next-line
export const vCloseModal: ObjectDirective<any> = {
	mounted(el, binding) {
		el.__CloseModalClick__ = (e: MouseEvent) => {
			if (!(el === e.target || el.contains(e.target))) {
				binding.value()
			}
		}

		el.__CloseModalKeydown__ = (e: KeyboardEvent) => {
			if (e.code === 'Escape') {
				binding.value()
			}
		}

		document.addEventListener('click', el.__CloseModalClick__)
		document.addEventListener('keydown', el.__CloseModalKeydown__)
	},
	unmounted(el) {
		document.removeEventListener('click', el.__CloseModalClick__)
		document.removeEventListener('keydown', el.__CloseModalKeydown__)
	}
}
