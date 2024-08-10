activate-venv:
	source .venv/bin/activate
create-venv:
	python3 -m venv .venv
check-git-version:
	git --version
install-os-git:
	sudo apt-get install git