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
list-pip:
	pip list
upgrade-pip:
	python3 -m pip install --upgrade pip
check-python-version:
	python3 --version
install-os-python:
	sudo apt-get install python3 python3-pip python3.11-venv
check-os-release:
	lsb_release -a
install-os-essential:
	sudo apt-get install lsb-release build-essential
run-os-upgrade:
	sudo apt-get upgrade
run-os-update:
	sudo apt-get update