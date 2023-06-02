document.addEventListener("DOMContentLoaded", () => {
	const storageKey = 'now_history'

	getHistory = () => {
		const history = localStorage.getItem(storageKey);
		return history ? JSON.parse(history) : []
	}

	updateHistory = () => {
		let history = getHistory()

		history = history.filter(item => item.url != document.URL)

		history.push({
			title: document.title,
			url: document.URL
		})

		if (history.length > 10)
			history = history.slice(history.length - 10, history.length)

		localStorage.setItem(storageKey, JSON.stringify(history))
	}

	updateHistoryMenu = e => {
		const children = getHistory().map(v => $(`<li><a href=${v.url}>${v.title}</a></li>`))
		children.push($('<li class="divider"></li>'))

		const clearHistButton = $('<li><a href="#">Clear history</a></li>')
		$(clearHistButton).children('a').click(() => localStorage.removeItem(storageKey))

		children.push(clearHistButton)

		const ul = $(e.relatedTarget).next('ul')
		ul.empty()
		ul.append(children)
	}

	updateHistory()
	$('#now-history-menu').on('show.bs.dropdown', updateHistoryMenu)
});
