activate-venv:
	source .venv/bin/activate
create-venv:
	python3 -m venv .venv
check-git-version:
	git --version
install-os-git:
	sudo apt-get install git
check-pip-version:
	pip --version
check-poetry-version:
	poetry --version
install-poetry:
	pipx install poetry
check-pipx-version:
	pipx --version
install-pipx:
	pip install pipx