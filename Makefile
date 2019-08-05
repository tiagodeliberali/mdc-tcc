.PHONY: environment
environment:
	@pyenv install -s 3.7.0
	@pyenv virtualenv 3.7.0 mdc-tcc
	@pyenv local mdc-tcc

.PHONY: install
install:
	@PYTHONPATH=. python -m pip install -U -r requirements.txt
