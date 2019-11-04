montreal-protocol-controlled-substances.csv: scripts/process.py
	./venv/bin/python scripts/process.py

venv:
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install pandas
	touch venv

clean:
	rm -rf montreal-protocol-controlled-substances.csv venv

.PHONY: clean
